import importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
TAG = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>|\[[^\]]*\]|\{[^}]*\}')


def skel(t):
    return ['[]' if mm.group(0).startswith('[') else mm.group(0) for mm in TAG.finditer(t)]


ch = sys.argv[1]


def arch(p):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); return m.TTARCH2(c)


a_en = arch(os.path.join(ROOT, '..', '原版英文档', 'Borderlands_pc_Borderlands%s_data.ttarch2' % ch))
a_zh = arch(os.path.join(ROOT, '..', '汉化成品', 'Borderlands_pc_chs_full_Borderlands%s.ttarch2' % ch))
en = {}
for e in a_en.entries:
    n = a_en.name(e)
    if n.endswith('_english.landb'):
        try:
            en[n] = landb.extract(a_en.data(e))
        except ValueError:
            pass
truns = 0
tents = 0
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        z = landb.extract(a_zh.data(e))
    except ValueError:
        continue
    seq, seen = [], set()
    for x in en[n]:
        if x['text'] in seen:
            continue
        seen.add(x['text']); seq.append(x['text'])
    V = {x['text']: y['text'] for x, y in zip(en[n], z)}
    runs = 0
    cur = False
    for i in range(len(seq) - 1):
        hit = skel(V[seq[i]]) == skel(seq[i + 1]) and skel(V[seq[i]]) != skel(seq[i])
        if hit and not cur:
            runs += 1
        cur = hit
    if runs:
        truns += runs
        print('  [%-48s] 错位段 %d' % (n, runs))
print('第 %s 章 合计错位段 %d' % (ch, truns))
