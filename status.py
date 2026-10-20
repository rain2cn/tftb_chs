#!/usr/bin/env python3
"""通用统计：列出归档内英文 .landb 的条目数/去重数/待译数（继承 tr/*.py 已有译文）。
用法: status.py <归档.ttarch2> [文件名子串过滤] [--json]
缓存: tr/*.py 变更后会自动重建 _work/merged.json。
"""
import importlib.util, os, sys
import makedict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
TR = os.path.join(HERE, 'tr')
CACHE = os.path.join(HERE, '_work', 'merged.json')

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    arch = sys.argv[1]
    filt = next((a for a in sys.argv[2:] if not a.startswith('--')), '')
    T = makedict.load()
    spec = importlib.util.spec_from_file_location('t', os.path.join(HERE, 'ttce.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    import landb
    c = m.TTContainer(arch, os.path.join(HERE, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    tot = need_all = 0; rows = []
    for e in a.entries:
        n = a.name(e)
        if not n.endswith('_english.landb') or (filt and filt not in n):
            continue
        d = a.data(e)
        try:
            S = landb.extract(d)
        except ValueError as ex:
            rows.append((n, -1, -1, -1, -1)); print('%-58s !! %s (字节 %d)' % (n, ex, len(d))); continue
        seen = {x['text'] for x in S}
        miss = sum(1 for t in seen if t not in T)
        keep = sum(1 for t in seen if t in T and T[t] == t)
        rows.append((n, len(S), len(seen), miss, keep))
        tot += len(S); need_all += miss
    for n, c1, c2, miss, keep in sorted(rows, key=lambda r: -r[3]):
        if c1 >= 0:
            print('%-58s %5d 条  去重 %5d  未声明 %5d  保留 %4d' % (n, c1, c2, miss, keep))
    print('字典键 %d | 合计条目 %d | 真正未译（未在字典中）%d' % (len(T), tot, need_all))

if __name__ == '__main__':
    main()
