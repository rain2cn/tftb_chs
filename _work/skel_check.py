import importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
# 完整骨架：^..^ / <..> / <<id:..>> / [..] / {..}
MARK = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>|\[[^\]]*\]|\{[^}]*\}')
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
print('=== 第 %s 章：骨架不一致（含 [ ] { } 标签）===' % ch)
tot = 0
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb') or n not in en:
        continue
    try:
        z = landb.extract(a_zh.data(e))
    except ValueError:
        continue
    hits = [(x['text'], y['text']) for x, y in zip(en[n], z) if MARK.findall(x['text']) != MARK.findall(y['text'])]
    if hits:
        tot += len(hits)
        print('  [%s] %d 处' % (n, len(hits)))
        for x, y in hits[:4]:
            print('     EN:', repr(x)[:80])
            print('     ZH:', repr(y)[:80])
print('合计 %d 处' % tot)
