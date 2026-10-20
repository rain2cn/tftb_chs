#!/usr/bin/env python3
"""方案 A：把 .font 里的位图字形图集用目标 TTF 的字形重绘（布局/度量完全不动）。

.font (MSV6) 结构（已实测）：
  [0:140)      MSV6 头：magic "6VSM" | u32 metaLen | u32 seg2Len | u32 texLen | u32
  [140:140+metaLen)  元数据：u32 16 | u32 8 | 字体名(NUL 前) | f32 height | f32 base | f32 | f32
                     | u32 (count*48+8) | u32 count
                     | 字形表：count 条，每条 48 字节
                        +0 codepoint(u32) +4 page(u32) +8 channel(u32)
                        +12 x1 +16 x2 +20 y1 +24 y2  (归一化 UV，TRect=(x1,x2,y1,y2))
                        +28 w +32 h +36 xOffset +40 yOffset +44 xAdvance
  [140+metaLen:]      位图图集：BC3/DXT5 原始块数据，长度 = texLen = W*H
                      颜色块恒为白(c0=0xFFFF,c1=0x0000,idx=0)，字形只存在于 alpha 块
"""
import os
import struct
import sys

GLYPH_STRIDE = 48
WHITE_COLOR_BLOCK = b'\xff\xff\x00\x00\x00\x00\x00\x00'


# ------------------------------------------------------------------ .font 解析
def parse_font(fb):
    meta_len, seg2, tex_len = struct.unpack_from('<III', fb, 4)
    meta = fb[140:140 + meta_len]
    name = meta[8:64].split(b'\x00')[0].decode('latin-1')
    table_off = 32 + len(name)
    height, base = struct.unpack_from('<2f', meta, 8 + len(name))
    count = struct.unpack_from('<I', meta, table_off - 4)[0]
    rows = []
    for k in range(count):
        o = table_off + GLYPH_STRIDE * k
        cp, page, chan = struct.unpack_from('<3I', meta, o)
        x1, x2, y1, y2 = struct.unpack_from('<4f', meta, o + 12)
        w, h, xo, yo, xa = struct.unpack_from('<5f', meta, o + 28)
        rows.append(dict(cp=cp, page=page, chan=chan, x1=x1, x2=x2, y1=y1, y2=y2,
                         w=w, h=h, xo=xo, yo=yo, xa=xa))
    return dict(meta_len=meta_len, tex_len=tex_len, name=name, table_off=table_off,
                height=height, base=base, count=count, rows=rows,
                atlas_off=140 + meta_len)


def guess_atlas_size(rows, tex_len):
    """图集是 W*H = tex_len，且 UV 矩形都对齐到整像素 -> 反推 W/H。"""
    best = None
    for w in (256, 512, 1024, 2048, 4096, 8192):
        if tex_len % w:
            continue
        h = tex_len // w
        if h > 8192 or h < 64:
            continue
        good = 0
        for r in rows:
            if r['w'] <= 0 or r['h'] <= 0:
                good += 1
                continue
            vals = (r['x1'] * w, r['x2'] * w, r['y1'] * h, r['y2'] * h)
            if all(abs(v - round(v)) < 0.01 for v in vals):
                good += 1
        score = good / len(rows)
        if best is None or score > best[0]:
            best = (score, w, h)
    return best  # (比例, W, H)


# ------------------------------------------------------------------ BC3
def decode_bc3_alpha(data, W, H):
    out = bytearray(W * H)
    bw = W // 4
    n = len(data) // 16
    for i in range(n):
        o = i * 16
        a0 = data[o]
        a1 = data[o + 1]
        bits = int.from_bytes(data[o + 2:o + 8], 'little')
        pal = [a0, a1, 0, 0, 0, 0, 0, 0]
        if a0 > a1:
            for k in range(1, 7):
                pal[1 + k] = ((7 - k) * a0 + k * a1) // 7
        else:
            for k in range(1, 5):
                pal[1 + k] = ((5 - k) * a0 + k * a1) // 5
            pal[6] = 0
            pal[7] = 255
        bx = (i % bw) * 4
        by = (i // bw) * 4
        base = by * W + bx
        for j in range(16):
            out[base + (j >> 2) * W + (j & 3)] = pal[(bits >> (3 * j)) & 7]
    return out


def encode_bc3_alpha(alpha, W, H, cache=None, log=None, orig_data=None, orig_alpha=None):
    """alpha: W*H 灰度；返回 BC3 块数据（颜色块恒白）。

    若给出 orig_data/orig_alpha：没被改动的块直接沿用原始 16 字节，
    这样未触碰的格子（含跳过的缺字）与原文件逐字节一致，改动只落在真正重绘的块上。
    """
    if cache is None:
        cache = {}
    out = bytearray()
    bw = W // 4
    reused = 0
    for by in range(0, H, 4):
        for bx in range(0, W, 4):
            base = by * W + bx
            vals = tuple(alpha[base + (j >> 2) * W + (j & 3)] for j in range(16))
            if orig_data is not None:
                ov = tuple(orig_alpha[base + (j >> 2) * W + (j & 3)] for j in range(16))
                if vals == ov:
                    i = (by // 4) * bw + (bx // 4)
                    out += orig_data[i * 16:(i + 1) * 16]
                    reused += 1
                    continue
            hit = cache.get(vals)
            if hit is None:
                vmin = min(vals)
                vmax = max(vals)
                if vmin == vmax:
                    hit = bytes((vmin, vmin, 0, 0, 0, 0, 0, 0)) + WHITE_COLOR_BLOCK
                else:
                    a0, a1 = vmax, vmin
                    pal = [a0, a1] + [((7 - k) * a0 + k * a1) // 7 for k in range(1, 7)]
                    idx = 0
                    for j in range(16):
                        v = vals[j]
                        best = 0
                        bd = 999
                        for k in range(8):
                            d = abs(pal[k] - v)
                            if d < bd:
                                bd = d
                                best = k
                        idx |= best << (3 * j)
                    hit = bytes((a0, a1)) + idx.to_bytes(6, 'little') + WHITE_COLOR_BLOCK
                cache[vals] = hit
            out += hit
        if log and by % 256 == 0:
            log('    编码行 %d/%d' % (by, H))
    if log and orig_data is not None:
        log('    未改动块直接沿用原始数据: %d / %d' % (reused, (W // 4) * (H // 4)))
    return bytes(out)


# ------------------------------------------------------------------ 重绘
def ttf_cmap(ttf_path):
    """返回目标字体的码点集合（用于跳过缺字）；没有 fontTools 时返回 None。"""
    try:
        from fontTools.ttLib import TTFont
    except Exception:
        return None
    f = TTFont(ttf_path, lazy=True)
    cm = set()
    for t in f['cmap'].tables:
        try:
            cm |= set(t.cmap.keys())
        except Exception:
            pass
    return cm


def rebake_font(fb, ttf_path, em=None, log=print):
    from PIL import Image, ImageDraw, ImageFont
    info = parse_font(fb)
    score, W, H = guess_atlas_size(info['rows'], info['tex_len'])
    log('  %s: height=%.1f base=%.1f 字形=%d 图集=%dx%d(推断吻合度 %.3f)'
        % (info['name'], info['height'], info['base'], info['count'], W, H, score))
    data = fb[info['atlas_off']:info['atlas_off'] + info['tex_len']]
    # 校验颜色块是否全白（若不全白则保留原样）
    nonwhite = 0
    for i in range(0, len(data), 16):
        if data[i + 8:i + 16] != WHITE_COLOR_BLOCK:
            nonwhite += 1
    if nonwhite:
        log('  ! 有 %d 个颜色块不是纯白，将按原样保留' % nonwhite)
    alpha = decode_bc3_alpha(data, W, H)
    alpha_orig = bytearray(alpha)                  # 用于「未改动块沿用原始数据」

    cmap = ttf_cmap(ttf_path)

    em = em or int(round(info['base']))            # base == 原渲染尺寸的 ascent
    face = ImageFont.truetype(ttf_path, em)
    ascent, descent = face.getmetrics()
    pen_x = em
    baseline = em + ascent
    canvas = Image.new('L', (em * 4, em * 4), 0)
    draw = ImageDraw.Draw(canvas)

    # 第一遍：渲染并测 ink，定全局缩放（保证不越界）
    items = []
    scales = []
    skipped = []
    for r in info['rows']:
        cw = int(round(r['w']))
        ch = int(round(r['h']))
        if cw <= 0 or ch <= 0 or r['cp'] > 0x10FFFF:
            continue
        if cmap is not None and r['cp'] not in cmap:      # 目标字体没有这个字 -> 保留原字形
            skipped.append(r['cp'])
            continue
        px1, py1 = int(round(r['x1'] * W)), int(round(r['y1'] * H))
        px2, py2 = int(round(r['x2'] * W)), int(round(r['y2'] * H))
        draw.rectangle([0, 0, canvas.width, canvas.height], fill=0)
        try:
            draw.text((pen_x, baseline), chr(r['cp']), font=face, fill=255, anchor='ls')
        except Exception:
            continue
        bb = canvas.getbbox()
        if not bb:
            continue
        gw, gh = bb[2] - bb[0], bb[3] - bb[1]
        # 记录：像素框、新 ink 的偏置(相对 penX / em 顶)
        items.append((r, px1, py1, px2, py2, bb[0] - pen_x, bb[1] - em, gw, gh))
        scales.append(min(1.0, (px2 - px1) / max(1, gw), (py2 - py1) / max(1, gh)))
    scales.sort()
    scale = 1.0
    if scales:
        scale = scales[len(scales) // 2]            # 取中位数，避免个别大字形把整体拖小
    scale = max(min(scale, 1.0), 0.60)
    log('  渲染 %d 个字形，全局缩放 %.3f%s'
        % (len(items), scale,
           ('，跳过缺字 %d 个（保留原字形）' % len(skipped)) if skipped else ''))

    # 第二遍：先清空原格子，再贴新字形（否则旧字形会残留一圈像素）
    for (r, px1, py1, px2, py2, xo2, yo2, gw, gh) in items:
        for yy in range(py1, py2):
            off = yy * W + px1
            alpha[off:off + (px2 - px1)] = b'\x00' * (px2 - px1)
        draw.rectangle([0, 0, canvas.width, canvas.height], fill=0)
        draw.text((pen_x, baseline), chr(r['cp']), font=face, fill=255, anchor='ls')
        bb = canvas.getbbox()
        g = canvas.crop(bb)
        s = min(scale, (px2 - px1) / max(1, g.width), (py2 - py1) / max(1, g.height))
        s = max(s, 0.35)
        if abs(s - 1.0) > 0.01:
            g = g.resize((max(1, int(round(g.width * s))), max(1, int(round(g.height * s)))),
                         Image.LANCZOS)
        tx = px1 + int(round(xo2 - r['xo']))
        ty = py1 + int(round(yo2 - r['yo']))
        tx = min(max(tx, px1), px2 - g.width)
        ty = min(max(ty, py1), py2 - g.height)
        if g.width <= 0 or g.height <= 0:
            continue
        gb = g.tobytes()
        for yy in range(g.height):
            row = ty + yy
            if row < 0 or row >= H:
                continue
            x0 = max(tx, 0)
            x1 = min(tx + g.width, W)
            if x1 <= x0:
                continue
            off = row * W + x0
            alpha[off:off + (x1 - x0)] = gb[yy * g.width + (x0 - tx):yy * g.width + (x1 - tx)]

    newtex = encode_bc3_alpha(alpha, W, H, log=log, orig_data=data, orig_alpha=alpha_orig)
    assert len(newtex) == info['tex_len'], (len(newtex), info['tex_len'])
    return fb[:info['atlas_off']] + newtex, (W, H), alpha


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        print('用法: python3 rebake.py <输入目录(含 .font)> <输出目录> <字体文件.ttf>')
        sys.exit(1)
    src, dst, ttf = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(dst, exist_ok=True)
    for n in sorted(os.listdir(src)):
        if not n.lower().endswith('.font'):
            continue
        fb = open(os.path.join(src, n), 'rb').read()
        print('== %s (%d 字节)' % (n, len(fb)))
        out, (W, H), alpha = rebake_font(fb, ttf)
        open(os.path.join(dst, n), 'wb').write(out)
        print('   -> %s (%d 字节, 图集 %dx%d)' % (os.path.join(dst, n), len(out), W, H))


if __name__ == '__main__':
    main()
