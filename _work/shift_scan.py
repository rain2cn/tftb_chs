import importlib.util, os, re, sys, ast
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
TAG = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>|\[[^\]]*\]|\{[^}]*\}')
ch, res = sys.argv[1], sys.argv[2]


def skel(t):
    return ['[]' if mm.group(0).startswith('[') else mm.group(0) for mm in TAG.finditer(t)]


def one(p, n):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    for e in a.entries:
        if a.name(e) == n:
            return landb.extract(a.data(e))


EN = one(os.path.join(ROOT, '..', '原版英文档', 'Borderlands_pc_Borderlands%s_data.ttarch2' % ch), res)
ZH = one(os.path.join(ROOT, '..', '汉化成品', 'Borderlands_pc_chs_full_Borderlands%s.ttarch2' % ch), res)
seq, seen = [], set()
for x in EN:
    if x['text'] in seen:
        continue
    seen.add(x['text']); seq.append(x['text'])
V = {}
for x, y in zip(EN, ZH):
    V[x['text']] = y['text']
runs = []
cur = None
for i in range(len(seq) - 1):
    a, b = seq[i], seq[i + 1]
    if skel(V[a]) == skel(b) and skel(V[a]) != skel(a):
        if cur is None:
            cur = [i, i]
        else:
            cur[1] = i
    else:
        if cur:
            runs.append(cur); cur = None
if cur:
    runs.append(cur)
print('资源 %s：去重 %d，疑似「值=下一条译文」的错位区间 %d 段' % (res, len(seq), len(runs)))
for s, e in runs:
    print('   区间 [%d..%d]（%d 条）示例: %r -> %r' % (s, e, e - s + 1, seq[s][:50], V[seq[s]][:50]))
