#!/usr/bin/env python3
"""校验重绘结果是否「干净」：逐个字形比对「应有的像素」与「图集里实际的像素」。

用法:
    .venv/bin/python verify.py <原始包.ttarch2> <新包.ttarch2> <字体名,如 Rockwell.font> [字体.ttf]

判定（独立于 rebake.py 重算一遍，避免同源错误）：
  1. 按同样规则渲染目标 TTF 的该字形 -> 得到「这个格子应该长什么样」；
  2. 格子内 actual>64 而 expected<32  = 旧字形残留；
     expected>64 而 actual<32         = 新字形被裁掉；
  3. 被跳过的缺字格子应与原图集逐字节一致（因为未改动的块会沿用原始数据）。
BC3 量化会把 0 精确保留为 0（含 0 的块 a1=min=0），所以可以直接按像素判定。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ttce          # noqa: E402
import atlas         # noqa: E402
import rebake        # noqa: E402

HI, LO = 64, 32


def load_font(archive, name):
    c = ttce.TTContainer(archive, os.path.join(HERE, 'TTL_Blowfish.h'))
    a = ttce.TTARCH2(c)
    for e in a.entries:
        if a.name(e) == name:
            return a.data(e)
    raise KeyError(name)


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    src, dst, fname = sys.argv[1], sys.argv[2], sys.argv[3]
    ttf = sys.argv[4] if len(sys.argv) > 4 else os.path.join(HERE, '..', 'alifangyuan.ttf')

    from PIL import Image, ImageDraw, ImageFont
    fb_old = load_font(src, fname)
    fb_new = load_font(dst, fname)
    info = rebake.parse_font(fb_new)
    score, W, H = rebake.guess_atlas_size(info['rows'], info['tex_len'])
    print('%s: %s  图集 %dx%d  字形 %d' % (fname, info['name'], W, H, info['count']))

    al_old = atlas.bc3_alpha(fb_old[info['atlas_off']:info['atlas_off'] + info['tex_len']], W, H)
    al_new = atlas.bc3_alpha(fb_new[info['atlas_off']:info['atlas_off'] + info['tex_len']], W, H)

    cmap = rebake.ttf_cmap(ttf)
    em = int(round(info['base']))
    face = ImageFont.truetype(ttf, em)
    ascent, _ = face.getmetrics()
    pen_x, baseline = em, em + ascent
    canvas = Image.new('L', (em * 4, em * 4), 0)
    draw = ImageDraw.Draw(canvas)

    # 与 rebake 相同的规则：先定全局缩放
    items, scales = [], []
    for r in info['rows']:
        if r['w'] <= 0 or r['h'] <= 0 or (cmap is not None and r['cp'] not in cmap):
            continue
        draw.rectangle([0, 0, canvas.width, canvas.height], fill=0)
        try:
            draw.text((pen_x, baseline), chr(r['cp']), font=face, fill=255, anchor='ls')
        except Exception:
            continue
        bb = canvas.getbbox()
        if not bb:
            continue
        px1, py1 = int(round(r['x1'] * W)), int(round(r['y1'] * H))
        px2, py2 = int(round(r['x2'] * W)), int(round(r['y2'] * H))
        gw, gh = bb[2] - bb[0], bb[3] - bb[1]
        items.append((r, px1, py1, px2, py2, bb[0] - pen_x, bb[1] - em, gw, gh))
        scales.append(min(1.0, (px2 - px1) / max(1, gw), (py2 - py1) / max(1, gh)))
    scales.sort()
    scale = max(min(scales[len(scales) // 2], 1.0), 0.60) if scales else 1.0

    residue = clip = 0
    worst = []
    for (r, px1, py1, px2, py2, xo2, yo2, gw, gh) in items:
        draw.rectangle([0, 0, canvas.width, canvas.height], fill=0)
        draw.text((pen_x, baseline), chr(r['cp']), font=face, fill=255, anchor='ls')
        g = canvas.crop(canvas.getbbox())
        s = max(min(scale, (px2 - px1) / max(1, g.width), (py2 - py1) / max(1, g.height)), 0.35)
        if abs(s - 1.0) > 0.01:
            g = g.resize((max(1, int(round(g.width * s))), max(1, int(round(g.height * s)))),
                         Image.LANCZOS)
        tx = min(max(px1 + int(round(xo2 - r['xo'])), px1), px2 - g.width)
        ty = min(max(py1 + int(round(yo2 - r['yo'])), py1), py2 - g.height)
        gb = g.tobytes()
        res = cl = 0
        for y in range(py1, min(py2, H)):
            row = y * W
            gy = y - ty
            inrow = 0 <= gy < g.height
            for x in range(px1, min(px2, W)):
                exp = gb[gy * g.width + (x - tx)] if (inrow and 0 <= x - tx < g.width) else 0
                act = al_new[row + x]
                if act > HI and exp < LO:
                    res += 1
                elif exp > HI and act < LO:
                    cl += 1
        residue += res
        clip += cl
        if res or cl:
            worst.append((res + cl, r['cp'], res, cl))
    worst.sort(reverse=True)

    kept = kept_diff = 0
    kept_maxdelta = 0
    if cmap is not None:
        for r in info['rows']:
            if r['w'] <= 0 or r['h'] <= 0 or r['cp'] in cmap:
                continue
            kept += 1
            px1, py1 = int(round(r['x1'] * W)), int(round(r['y1'] * H))
            px2, py2 = int(round(r['x2'] * W)), int(round(r['y2'] * H))
            mx = 0
            for y in range(py1, min(py2, H)):
                row = y * W
                for x in range(px1, min(px2, W)):
                    d = abs(al_old[row + x] - al_new[row + x])
                    if d > mx:
                        mx = d
            kept_maxdelta = max(kept_maxdelta, mx)
            # 只把「超过量化噪声」的差异算作不一致（BC3 八级量化 + 邻格块重编码噪声 <=24）
            if mx > 24:
                kept_diff += 1

    print('  旧字形残留像素: %d　新字形被裁像素: %d' % (residue, clip))
    if worst:
        print('  最严重 10 个: %s'
              % ', '.join('U+%04X(残留%d/裁%d)' % (c, n1, n2) for _, c, n1, n2 in worst[:10]))
    print('  跳过(缺字)字形: %d 个，超出量化噪声的不一致: %d（最大灰度差 %d）'
          % (kept, kept_diff, kept_maxdelta))
    clean = (residue == 0 and clip == 0 and kept_diff == 0)
    print('  结论：%s' % ('图集干净：无旧字形残留、无裁切、缺字保留原样'
                        if clean else '存在问题，见上'))


if __name__ == '__main__':
    main()
