import importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
SKIP = re.compile(r'\.(chore|style|lua|font|prop|scene|d3dtx)|<<author>>|<<date|^-\s|author,|CHORE|NOTE:|IDEA|VFX|ANM:|^sk\d')
ch = sys.argv[1]


def one(p):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    return a


a_en = one(os.path.join(ROOT, '..', '原版英文档', 'Borderlands_pc_Borderlands%s_data.ttarch2' % ch))
a_zh = one(os.path.join(ROOT, '..', '汉化成品', 'Borderlands_pc_chs_full_Borderlands%s.ttarch2' % ch))
en = {}
for e in a_en.entries:
    n = a_en.name(e)
    if n.endswith('_english.landb'):
        try:
            en[n] = landb.extract(a_en.data(e))
        except ValueError:
            pass
hits = []
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        z = landb.extract(a_zh.data(e))
    except ValueError:
        continue
    for x, y in zip(en[n], z):
        t = y['text']
        if t != x['text'] or re.search(r'[\u4e00-\u9fff]', t):
            continue
        s = re.sub(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>|\^[^\^]*\^', '', t).strip()
        if len(s) < 12 or ' ' not in s or not re.search(r'[a-z]', s):
            continue
        if s.upper() == s or SKIP.search(s):
            continue
        hits.append((n, s))
print('第%s章 真漏译候选 %d 条' % (ch, len(hits)))
for k, s in hits[:15]:
    print('   [%s] %r' % (k[:26], s[:95]))
