"""列出 tr/*.py 里「括号内含中文」的条目，给出文件:行号、当前括号内容、以及原文对应的英文标记。
输出：_work/括号待修清单.tsv 与 括号待修清单.md
"""
import ast, glob, io, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
CJK = re.compile(r'[\u4e00-\u9fff]')
TOK = re.compile(r'\[[^\]]*\]|\{[^}]*\}')

rows = []
for p in sorted(glob.glob('tr/*.py')):
    if os.path.basename(p).startswith('_'):
        continue
    src = io.open(p, encoding='utf-8').read()
    try:
        tree = ast.parse(src, p)
    except SyntaxError:
        continue
    lines = src.split('\n')
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and isinstance(v, ast.Constant)):
                continue
            if not (isinstance(k.value, str) and isinstance(v.value, str)):
                continue
            bad = [t for t in TOK.findall(v.value) if CJK.search(t)]
            if not bad:
                continue
            et, zt = TOK.findall(k.value), TOK.findall(v.value)
            sugg = []
            for t in zt:
                if CJK.search(t):
                    i = zt.index(t)
                    sugg.append(et[i] if i < len(et) else '（原文无对应）')
                else:
                    sugg.append(t)
            rows.append(dict(file=p, line=k.lineno, bad=bad, sugg=sugg,
                             zh=v.value[:60].replace('\n', '\\n'),
                             en=k.value[:60].replace('\n', '\\n'),
                             text=lines[k.lineno - 1].strip()[:160]))

# 标出"有效"的那条（同名 EN 键最后出现的文件才生效）
last = {}
for r in rows:
    last[r['en']] = r['file']
for r in rows:
    r['effective'] = (last[r['en']] == r['file'])

os.makedirs('_work', exist_ok=True)
with io.open('_work/括号待修清单.tsv', 'w', encoding='utf-8') as f:
    f.write('文件\t行号\t是否生效\t当前括号内容\t建议改成\t英文原文（前60字）\n')
    for r in rows:
        f.write('%s\t%d\t%s\t%s\t%s\t%s\n' % (
            r['file'], r['line'], '生效' if r['effective'] else '被后面的文件覆盖',
            ' '.join(r['bad']), ' '.join(r['sugg']), r['en']))

with io.open('_work/括号待修清单.md', 'w', encoding='utf-8') as f:
    f.write('# 括号内含中文的条目清单\n\n')
    f.write('共 %d 处。「生效」= 该文件里的这条是最终生效值（后面的文件会覆盖同名键）。\n\n' % len(rows))
    cur = None
    for r in rows:
        if r['file'] != cur:
            cur = r['file']
            f.write('\n## %s\n\n' % cur)
        f.write('- **第 %d 行**%s  \n  当前：`%s` → 建议：`%s`  \n  原文：`%s`\n' % (
            r['line'], '' if r['effective'] else '（被后面覆盖，可忽略）',
            ' '.join(r['bad']), ' '.join(r['sugg']), r['en']))

print('共 %d 处；按文件统计：' % len(rows))
from collections import Counter
for p, n in Counter(r['file'] for r in rows).most_common():
    eff = sum(1 for r in rows if r['file'] == p and r['effective'])
    print('  %-52s %3d 处（其中生效 %d）' % (p, n, eff))
print('\n已写：_work/括号待修清单.tsv 、_work/括号待修清单.md')
