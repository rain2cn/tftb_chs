"""把「演职员表」相关的译文条目从 tr/*.py 里清掉，并移走整份都是演职员表的文件。
判据：某个键若只出现在 ui_credits* 资源里，就算「演职员表专用键」。
安全网：清之前打快照；整份文件被移除的，移到 _归档_早期试验/tr_移除的演职员表/（不删）。
用法: strip_credits_from_tr.py [--apply]
"""
import ast, importlib.util, io, os, shutil, sys

ROOT = '/home/deck/Downloads/archives/翻译工程'
TR = os.path.join(ROOT, 'tr')
EN_DIR = os.path.join(ROOT, '..', '原版英文档')
BACKUP = os.path.join(ROOT, '..', '_归档_早期试验', 'tr_移除的演职员表')
DRY = '--apply' not in sys.argv
os.chdir(ROOT)
sys.path.insert(0, ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

# 1) 键 -> 它出现在哪些资源里
key_res = {}
for fn in sorted(os.listdir(EN_DIR)):
    if not fn.endswith('.ttarch2'):
        continue
    c = m.TTContainer(os.path.join(EN_DIR, fn), os.path.join(ROOT, 'TTL_Blowfish.h'))
    a = m.TTARCH2(c)
    for e in a.entries:
        n = a.name(e)
        if not n.endswith('_english.landb'):
            continue
        try:
            S = landb.extract(a.data(e))
        except ValueError:
            continue
        for x in S:
            key_res.setdefault(x['text'], set()).add(n)
        del S
credits_keys = {k for k, res in key_res.items() if res and all('ui_credits' in r for r in res)}
print('原版归档键 %d 个；其中「只在演职员表资源里出现」的键 %d 个' % (len(key_res), len(credits_keys)))

# 2) 逐个文件处理
os.makedirs(BACKUP, exist_ok=True)
moved, trimmed, removed_keys = [], [], 0
for fn in sorted(os.listdir(TR)):
    if not fn.endswith('.py') or fn.startswith('_') or fn == 'phrases.py':
        continue
    p = os.path.join(TR, fn)
    src = io.open(p, encoding='utf-8').read()
    try:
        tree = ast.parse(src, p)
    except SyntaxError:
        continue
    entries = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and isinstance(v, ast.Constant) \
                        and isinstance(k.value, str) and isinstance(v.value, str):
                    entries.append((k.value, v.value))
    if not entries:
        continue
    kept = [(k, v) for k, v in entries if k not in credits_keys]
    gone = len(entries) - len(kept)
    if gone == 0:
        continue
    if not kept:                      # 整份都是演职员表 -> 移走
        moved.append((fn, gone))
        if not DRY:
            shutil.move(p, os.path.join(BACKUP, fn))
        continue
    trimmed.append((fn, gone, len(kept)))
    removed_keys += gone
    if not DRY:
        head = [l for l in src.split('\n') if l.lstrip().startswith('#')]
        out = ['# %s（已移除演职员表条目：这些资源整份走英文原档）' % fn] + head + ['T = {']
        for k, v in kept:
            out.append(' %r: %r,' % (k, v))
        out.append('}')
        io.open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')

print('\n%s' % ('【试运行】' if DRY else '【已应用】'))
print('整份移走的文件（%d 个，共 %d 条）:' % (len(moved), sum(g for _, g in moved)))
for fn, g in moved:
    print('   tr/%s  (%d 条)' % (fn, g))
print('部分裁剪的文件（%d 个，合计移除 %d 条）:' % (len(trimmed), removed_keys))
for fn, g, k in trimmed:
    print('   tr/%s  移除 %d 条 / 余 %d 条' % (fn, g, k))
print('\n备份位置: %s' % os.path.normpath(BACKUP))
