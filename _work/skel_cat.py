import importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
TAG = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>|\[[^\]]*\]|\{[^}]*\}')


def skel(t, norm):
    out = []
    for mm in TAG.finditer(t):
        g = mm.group(0)
        if g.startswith('['):
            out.append('[]')
        else:
            out.append(re.sub(r'\s+', '', g) if norm else g)
    return out


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
ca = cb = 0
print('=== 第 %s 章 ===' % ch)
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        z = landb.extract(a_zh.data(e))
    except ValueError:
        continue
    A = B = 0
    bs = []
    for x, y in zip(en[n], z):
        if skel(x['text'], False) == skel(y['text'], False):
            continue
        if skel(x['text'], True) == skel(y['text'], True):
            A += 1
        else:
            B += 1
            if len(bs) < 3:
                bs.append((x['text'], y['text']))
    ca += A; cb += B
    if A or B:
        print('  [%-46s] 空格类 %d | 真错位 %d' % (n, A, B))
        for x, y in bs:
            print('      EN:', repr(x)[:88])
            print('      ZH:', repr(y)[:88])
print('合计：空格类 %d 处（可自动修） | 真错位 %d 处（需人工定位）' % (ca, cb))
