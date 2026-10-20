#!/usr/bin/env python3
"""导出某英文 .landb 中「尚未翻译」的唯一文本行（继承 tr/*.py 已有译文）。
用法: todo_lines.py <归档.ttarch2> <文件名或子串> [输出文件]
不给输出文件则打印到 stdout。
"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import landb, makedict

def main():
    arch, pat = sys.argv[1], sys.argv[2]
    out = sys.argv[3] if len(sys.argv) > 3 else None
    T = makedict.load()
    spec = importlib.util.spec_from_file_location('t', os.path.join(HERE, 'ttce.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = m.TTContainer(arch, os.path.join(HERE, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    for e in a.entries:
        n = a.name(e)
        if pat not in n: continue
        S = landb.extract(a.data(e)); seen = set(); lines = []
        for x in S:
            t = x['text']
            if t in seen: continue
            seen.add(t)
            if t in T and T[t] != t: continue
            lines.append(t.replace('\n', '\\n'))
        body = '\n'.join(lines) + ('\n' if lines else '')
        if out:
            open(out, 'w', encoding='utf-8').write(body); print('%s -> %s: 待译 %d 条' % (n, out, len(lines)))
        else:
            sys.stdout.write(body)
        return
    print('未找到匹配 %s' % pat, file=sys.stderr)

if __name__ == '__main__':
    main()
