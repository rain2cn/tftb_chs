#!/usr/bin/env python3
"""Telltale `.landb`（本地化文本库）解析 / 提取 / 回写。

容器（实测）：
  [0..140)   MSV6 头: "6VSM" | u32 metaLen | u32 seg2Len | u32 texLen(=0) | u32=10 | 120 字节常量块
  [140..140+metaLen)   记录区（下面详述）
  [140+metaLen..)      字符串池：u32 长度前缀的字符串（音频名等，如 "295772161.lang"）

记录区内部：
  [u32 sec1头][每条: 记录 + 68 字节「附加块」]...[48 字节尾部]
  记录  = [u32 记录总长(含自身)][u32 8][u32 0] + 若干「字符串块」 + [u32 8][u32 1]
  字符串块 = [u32 块长(=8+文本字节数)][u32 文本字节数][UTF-8 文本]
  附加块/尾部与本条文本长度无关（只含 id 与哈希），回写时原样保留。

因此改文本只需：改文本字节 + 修正块长 → 修正所在记录总长 → 修正 metaLen。
本脚本的回写采用「按块定位 + 顺序拼接」，不假设头部/附加块/尾部的固定长度。
"""
import re
import struct
import sys

HEADER = 140
CTRL = re.compile(r'[\x00-\x08\x0b-\x1f]')


def parse_header(data):
    if data[0:4] != b'6VSM':
        raise ValueError('不是 MSV6 容器: %r' % data[0:4])
    meta_len, seg2_len, tex_len, ver = struct.unpack_from('<4I', data, 4)
    return dict(meta_len=meta_len, seg2_len=seg2_len, tex_len=tex_len, version=ver)


def u32(buf, off):
    return struct.unpack_from('<I', buf, off)[0]


def solve_layout(body):
    """求解记录区布局：返回 (头部长度, 记录间附加块长度, 尾部长度)。

    已见的两种：普通文本库 (80, 68, 48)；credits/episode 类 (16, 0, 16)。
    先试这两种，失败再做有界的通用搜索。
    规则：从头部开始按 [记录长][+附加块] 链式前进；最后一条记录之后只剩「尾部」。
    """
    n = len(body)

    def try_layout(H, E, T):
        if H + 12 + T > n:
            return None
        p = H
        steps = 0
        while True:
            if p + 4 > n:
                return None
            rs = u32(body, p)
            if rs < 12 or p + rs > n:
                return None
            steps += 1
            if p + rs + T == n:
                return (H, E, T)
            if p + rs + E + T > n or steps > 1_000_000:
                return None
            p += rs + E

    for cand in ((80, 68, 48), (16, 0, 16), (80, 68, 16), (80, 0, 48), (16, 68, 48)):
        r = try_layout(*cand)
        if r:
            return r
    for H in range(0, 160, 4):
        for E in range(0, 120):
            for T in range(0, 120):
                r = try_layout(H, E, T)
                if r:
                    return r
    return None


def walk_records(body, layout=None):
    """返回 ([(rec_hdr_off, rec_size)], (H,E,T))。"""
    if layout is None:
        layout = solve_layout(body)
        if layout is None:
            raise ValueError('无法求解 .landb 记录布局')
    H, E, T = layout
    n = len(body)
    recs = []
    p = H
    while True:
        rs = u32(body, p)
        if rs < 12 or p + rs > n:
            raise ValueError('记录链断裂 @%d' % p)
        recs.append((p, rs))
        if p + rs + T == n:
            return recs, (H, E, T)
        p += rs + E


def find_blocks(body):
    """扫描所有「字符串块」：返回 [(blk_off, blk_size, text_off, text_len, text)]"""
    out = []
    i = 0
    n = len(body)
    while i + 8 <= n:
        bs = u32(body, i)
        tl = u32(body, i + 4)
        if 8 + tl == bs and 0 < tl <= 200000 and i + bs <= n:
            raw = body[i + 8:i + 8 + tl]
            try:
                txt = raw.decode('utf-8')
            except UnicodeDecodeError:
                i += 1
                continue
            if not CTRL.search(txt):
                out.append((i, bs, i + 8, tl, txt))
                i += bs
                continue
        i += 1
    return out


def blocks_in(body, recs):
    """把文本块归属到记录：返回 {记录序号: [块...]}（越界块丢弃）"""
    owner = {}
    bl = find_blocks(body)
    idx = 0
    for k, (rh, rs) in enumerate(recs):
        while idx < len(bl) and bl[idx][0] < rh:
            idx += 1
        j = idx
        while j < len(bl) and bl[j][0] < rh + rs:
            if bl[j][0] + bl[j][1] <= rh + rs:
                owner.setdefault(k, []).append(bl[j])
            j += 1
        idx = j
    return owner, bl


def extract(data, min_len=1):
    h = parse_header(data)
    body = data[HEADER:HEADER + h['meta_len']]
    recs, layout = walk_records(body)
    owner, _ = blocks_in(body, recs)
    out = []
    for k, (rh, rs) in enumerate(recs):
        for (boff, bsize, toff, tlen, txt) in owner.get(k, []):
            if len(txt) >= min_len:
                out.append(dict(rec_hdr=HEADER + rh, rec_size=rs, block_off=HEADER + boff,
                                off=HEADER + toff, text=txt, raw_len=tlen))
    return out


def rebuild(data, repl, layout=None, verbose=False):
    """repl: {文本在文件中的偏移: 新文本}。返回 (新字节, 改动条数)。"""
    h = parse_header(data)
    ml = h['meta_len']
    body = data[HEADER:HEADER + ml]
    recs, layout = walk_records(body, layout)
    owner, _ = blocks_in(body, recs)
    out = bytearray(data[:HEADER])
    cursor = 0
    changed = 0
    for k, (rh, rs) in enumerate(recs):
        rec = bytearray(body[rh:rh + rs])
        delta = 0
        for (boff, bsize, toff, tlen, txt) in owner.get(k, []):
            if HEADER + toff not in repl:
                continue
            nb = repl[HEADER + toff].encode('utf-8')
            seg = struct.pack('<II', 8 + len(nb), len(nb)) + nb
            p = boff - rh + delta
            rec[p:p + bsize] = seg
            delta += len(seg) - bsize
            changed += 1
        if delta:
            struct.pack_into('<I', rec, 0, rs + delta)
        out += body[cursor:rh]
        out += rec
        cursor = rh + rs
    out += body[cursor:]
    struct.pack_into('<I', out, 4, len(out) - HEADER)
    out += data[HEADER + ml:HEADER + ml + h['seg2_len']]
    return bytes(out), changed


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        print('用法:')
        print('  landb.py scan   <文件.landb>')
        print('  landb.py dump   <文件.landb> <输出.tsv>')
        print('  landb.py apply  <文件.landb> <译文.tsv> <输出.landb>')
        print('  landb.py verify <文件.landb>')
        sys.exit(1)
    cmd = sys.argv[1]
    data = open(sys.argv[2], 'rb').read()
    if cmd == 'scan':
        h = parse_header(data)
        body = data[HEADER:HEADER + h['meta_len']]
        recs, layout = walk_records(body)
        items = extract(data)
        print('%s: metaLen=%d seg2=%d' % (sys.argv[2], h['meta_len'], h['seg2_len']))
        print('  布局 头%d/记录间附加块%d/尾部%d, 记录 %d 条, 文本 %d 块 / %d 字符'
              % (layout[0], layout[1], layout[2], len(recs), len(items),
                 sum(len(x['text']) for x in items)))
        for x in items[:8]:
            print('    @%-7d %s' % (x['off'], x['text'][:70].replace('\n', '\\n')))
    elif cmd == 'dump':
        items = extract(data)
        with open(sys.argv[3], 'w', encoding='utf-8') as f:
            f.write('#off\ttext\n')
            for x in items:
                f.write('%d\t%s\n' % (x['off'], x['text'].replace('\\', '\\\\')
                                      .replace('\t', '\\t').replace('\n', '\\n')))
        print('已导出 %d 条 -> %s' % (len(items), sys.argv[3]))
    elif cmd == 'apply':
        repl = {}
        with open(sys.argv[3], encoding='utf-8') as f:
            for line in f:
                if line.startswith('#') or '\t' not in line:
                    continue
                off, txt = line.rstrip('\n').split('\t', 1)
                txt = txt.replace('\\n', '\n').replace('\\t', '\t').replace('\\\\', '\\')
                repl[int(off)] = txt
        out, n = rebuild(data, repl)
        open(sys.argv[4], 'wb').write(out)
        print('已回写 %d 条 -> %s (%d 字节)' % (n, sys.argv[4], len(out)))
    elif cmd == 'verify':
        items = extract(data)
        out, n = rebuild(data, {x['off']: x['text'] for x in items})
        print('无损往返: %d 条 %d -> %d 字节, 逐字节一致=%s' % (n, len(data), len(out), data == out))
        # 长度变化测试
        repl = {items[0]['off']: items[0]['text'] + 'XXXXX'}
        out2, n2 = rebuild(data, repl)
        back = extract(out2)
        ok = any(x['text'] == items[0]['text'] + 'XXXXX' for x in back) and len(back) == len(items)
        print('改长度测试: 改 %d 条, 重解析得到 %d 条(原 %d), 新文本命中=%s'
              % (n2, len(back), len(items), ok))


if __name__ == '__main__':
    main()
