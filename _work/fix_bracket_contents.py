"""把译文里「括号内含中文」的标记恢复成原文（[] 是音效/动作 ID，{} 是表情 ID，引擎要拿去查表）。

规则：
  · 逐条比对 `[]` / `{}` 标记；译文里含中文的标记，按位置换成原文对应标记；
  · 若标记数量与原文不一致（说明结构已被破坏），该条**整条还原原文**；
  · 只改「值」，不动键；直接改原 tr 文件（git 提交后再跑）。

用法: fix_bracket_contents.py <章节号 103> [--apply]
"""
import ast, io, importlib.util, os, re, sys
ROOT = '/home/deck/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
CJK = re.compile(r'[\u4e00-\u9fff]')
TOK = re.compile(r'\[[^\]]*\]|\{[^}]*\}')
ch = sys.argv[1]
APPLY = '--apply' in sys.argv

en_p = os.path.join(ROOT, '..', '原版英文档', 'Borderlands_pc_Borderlands%s_data.ttarch2' % ch)
zh_p = os.path.join(ROOT, '..', '汉化成品', 'Borderlands_pc_chs_full_Borderlands%s.ttarch2' % ch)


def recs(p):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    return {a.name(e): a.data(e) for e in a.entries if a.name(e).endswith('_english.landb')}


EN = recs(en_p)
c = m.TTContainer(zh_p, os.path.join(ROOT, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
ZH = {a.name(e): a.data(e) for e in a.entries if a.name(e).endswith('_english.landb')}

# 目标：英文原文 -> 修正后的译文
target = {}
stats = {'fixed': 0, 'revert': 0}
for n in sorted(ZH):
    if n not in EN:
        continue
    E = landb.extract(EN[n]); S = landb.extract(ZH[n])
    if len(E) != len(S):
        continue
    for x, y in zip(E, S):
        et, zt = TOK.findall(x['text']), TOK.findall(y['text'])
        if not any(CJK.search(t) for t in zt):
            continue
        if len(et) != len(zt):
            target[x['text']] = x['text']; stats['revert'] += 1
            print('  还原整条 [%s] %r' % (n[:24], x['text'][:50]))
            continue
        out = y['text']
        for i, t in enumerate(zt):
            if CJK.search(t):
                out = out.replace(t, et[i], 1)
        target[x['text']] = out; stats['fixed'] += 1
        print('  修标记 [%s] %r -> %r' % (n[:24], y['text'][:50], out[:50]))

print('\n共需处理 %d 条（修标记 %d / 整条还原 %d）' % (len(target), stats['fixed'], stats['revert']))
if not APPLY:
    print('（试运行；加 --apply 才会写入原 tr 文件）')
    sys.exit(0)

# 写回原 tr 文件：按 EN 键找到所在的 dict 值，原位替换字面量
files = ['tr/%s' % f for f in os.listdir('tr') if re.match(r'ep%d_' % int(ch[-1]), f) and f.endswith('.py')]
changed = 0
for p in files:
    src = io.open(p, encoding='utf-8').read()
    tree = ast.parse(src, p)
    edits = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and isinstance(v, ast.Constant)):
                continue
            if k.value in target and target[k.value] != v.value:
                edits.append((v, target[k.value]))
    if not edits:
        continue
    lines = src.split('\n')
    # 按 (行, 列) 精确定位值的字面量范围，逐条替换（同一行多处也安全）
    per_line = {}
    for v, newval in edits:
        per_line.setdefault(v.lineno - 1, []).append((v.col_offset, v.end_col_offset, repr(newval)))
    for ln, items in per_line.items():
        # 注意：ast 的 col_offset 是 **UTF-8 字节**偏移（含中文行必须按字节切）
        raw = lines[ln].encode('utf-8')
        for a, b, new_lit in sorted(items, key=lambda t: -t[0]):
            raw = raw[:a] + new_lit.encode('utf-8') + raw[b:]
            changed += 1
        lines[ln] = raw.decode('utf-8')
    io.open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('已改 %d 处，涉及 %d 个文件' % (changed, len(files)))
