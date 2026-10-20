"""按「整条记录」（同一条记录的各文本块拼接后）比对标记，能抓到跨块的标记问题。
用法: rec_marker_check.py <101|102|103|104|105|Menu>
"""
import importlib.util, os, re, sys, collections
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
MK = re.compile(r'<<[^>]*>>|<[^>]*>|\^[^\^]*\^|\{[^}]*\}')
tag = sys.argv[1]
nm = 'Borderlands' + tag if tag.isdigit() else tag


def recs(d):
    g = collections.OrderedDict()
    for x in landb.extract(d):
        g.setdefault(x['rec_hdr'], []).append(x['text'])
    return [''.join(v) for v in g.values()]


def arch(p):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); return m.TTARCH2(c)


a_en = arch(os.path.join(ROOT, '..', '原版英文档', 'Borderlands_pc_%s_data.ttarch2' % nm))
a_zh = arch(os.path.join(ROOT, '..', '汉化成品', 'Borderlands_pc_chs_full_%s.ttarch2' % nm))
en = {}
for e in a_en.entries:
    n = a_en.name(e)
    if n.endswith('_english.landb'):
        try:
            en[n] = recs(a_en.data(e))
        except ValueError:
            pass
tot = 0
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        B = recs(a_zh.data(e))
    except ValueError:
        continue
    A = en[n]
    if len(A) != len(B):
        print('  [%s] 记录数不同 EN %d vs 我们 %d' % (n, len(A), len(B))); continue
    shown = 0
    for a, b in zip(A, B):
        ca = collections.Counter(MK.findall(a)); cb = collections.Counter(MK.findall(b))
        if (ca - cb) or (cb - ca):
            tot += 1
            if shown < 2:
                print('  [%s]' % n[:30])
                print('     EN:', repr(a)[:78])
                print('     ZH:', repr(b)[:78])
                print('     少:', dict(ca - cb), ' 多:', dict(cb - ca))
            shown += 1
print('%s：整条记录标记差异合计 %d 处' % (nm, tot))
