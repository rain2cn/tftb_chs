import importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
TAG = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>|\[[^\]]*\]|\{[^}]*\}')


def skel(t):
    """返回标记类型序列：[] 只记个数（内容可译），其余必须完全一致。"""
    out = []
    for mm in TAG.finditer(t):
        g = mm.group(0)
        out.append('[]' if g.startswith('[') else g)
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
tot = 0
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        z = landb.extract(a_zh.data(e))
    except ValueError:
        continue
    hits = [(x['text'], y['text']) for x, y in zip(en[n], z) if skel(x['text']) != skel(y['text'])]
    if hits:
        tot += len(hits)
        print('  [%-46s] %d 处' % (n, len(hits)))
        for x, y in hits[:3]:
            print('     EN:', repr(x)[:90])
            print('     ZH:', repr(y)[:90])
print('第 %s 章 真实结构问题合计 %d 处' % (ch, tot))
