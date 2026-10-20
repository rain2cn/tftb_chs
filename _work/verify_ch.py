#!/usr/bin/env python3
"""逐章核验：产物 vs 原版英文档 —— 标记一致性 / 制表符一致性 / 含中文比例。
内存友好：只解包 _english.landb 资源，且逐个资源比对。
"""
import gc, importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
import landb
spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PM = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>')
ch = sys.argv[1]


def arch(p):
    c = m.TTContainer(p, os.path.join(ROOT, 'TTL_Blowfish.h')); return m.TTARCH2(c)


a_en = arch('../原版英文档/Borderlands_pc_Borderlands%s_data.ttarch2' % ch)
en = {}
for e in a_en.entries:
    n = a_en.name(e)
    if n.endswith('_english.landb'):
        try:
            en[n] = landb.extract(a_en.data(e))
        except ValueError:
            pass
a_zh = arch('../汉化成品/Borderlands_pc_chs_full_Borderlands%s.ttarch2' % ch)
tot = zhc = bad = tab = res = 0
for e in a_zh.entries:
    n = a_zh.name(e)
    if not n.endswith('_english.landb'):
        continue
    if n not in en:
        print('  !! 找不到对应英文资源 %s' % n); continue
    x = en[n]
    try:
        y = landb.extract(a_zh.data(e))
    except ValueError as ex:
        print('  !! 产物无法解析 %s (%s)' % (n, ex)); continue
    if len(x) != len(y):
        print('  !! 条目数不一致 %s %d/%d' % (n, len(x), len(y))); continue
    res += 1
    for u, v in zip(x, y):
        tot += 1
        if re.search(r'[\u4e00-\u9fff]', v['text']):
            zhc += 1
        if PM.findall(u['text']) != PM.findall(v['text']):
            bad += 1
        if u['text'].count('\t') != v['text'].count('\t'):
            tab += 1
gc.collect()
print('%s: 资源 %2d | 条目 %6d | 含中文 %6d (%4.1f%%) | 标记差异 %d | 制表符差 %d'
      % (ch, res, tot, zhc, 100.0 * zhc / max(tot, 1), bad, tab))
