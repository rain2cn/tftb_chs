#!/usr/bin/env python3
"""通用：为某个 ui_credits 类 .landb 生成译文字典（只译职务标签，人名/公司名保留），并报告未覆盖标签。
用法: gen_credits.py <归档.ttarch2> <英文文件名子串> <输出 tr 文件>
"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import landb
from credits_labels import LABELS as _L, KEEP
LABELS = {k.strip(): v for k, v in _L.items()}

def esc(s):
    return s.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def main():
    arch, pat, out = sys.argv[1], sys.argv[2], sys.argv[3]
    spec = importlib.util.spec_from_file_location('t', os.path.join(HERE, 'ttce.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = m.TTContainer(arch, os.path.join(HERE, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    for e in a.entries:
        n = a.name(e)
        if pat not in n: continue
        S = landb.extract(a.data(e))
        pairs = []; missing = []; replaced = 0
        for x in S:
            t = x['text']
            if not ('\n' in t and 'PRODUCTION TEAM' in t or t.strip() in LABELS or t.strip() in KEEP):
                pairs.append((t, t)); continue
            lines = t.split('\n'); outp = []
            for ln in lines:
                st = ln.strip()
                if st in LABELS:
                    outp.append(ln.replace(st, LABELS[st])); replaced += 1
                else:
                    if st and re.fullmatch(r"[A-Z0-9 &.,'\"\-/()+:!?]+", st) and len(st) > 2 and st not in KEEP:
                        missing.append(st)
                    outp.append(ln)
            pairs.append((t, '\n'.join(outp)))
        with open(out, 'w', encoding='utf-8') as f:
            f.write('# %s 译文（演职员表：仅译职务标签，人名/公司名保留）\nT = {\n' % n)
            for en, zh in pairs:
                f.write('    "%s":\n        "%s",\n' % (esc(en), esc(zh)))
            f.write('}\n')
        print('%s -> %s（%d 条；职务标签替换 %d 处）' % (n, out, len(pairs), replaced))
        if missing:
            print('未映射的大写标签（如需翻译请补进 credits_labels.py）:')
            for s2 in sorted(set(missing)): print('   |' + s2)
        return
    print('未找到匹配 %s' % pat, file=sys.stderr)

if __name__ == '__main__':
    main()
