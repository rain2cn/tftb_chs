#!/usr/bin/env python3
"""校验译文 landb：真实标记一致性、含中文条数、制表符数一致性。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import landb
en = landb.extract(open(sys.argv[1], 'rb').read())
zh = landb.extract(open(sys.argv[2], 'rb').read())
pm = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>')
bad = 0
for x, y in zip(en, zh):
    if pm.findall(x['text']) != pm.findall(y['text']):
        bad += 1
        if bad <= 3: print('  差异 英=%r 中=%r' % (x['text'][:80], y['text'][:80]))
zhc = sum(1 for y in zh if re.search(r'[\u4e00-\u9fff]', y['text']))
tab = sum(1 for x, y in zip(en, zh) if x['text'].count('\t') != y['text'].count('\t'))
print('%s：条数 %d/%d；真实标记不一致 %d；含中文 %d；制表符不一致 %d'
      % (os.path.basename(sys.argv[1]).replace('Ep1__', ''), len(zh), len(en), bad, zhc, tab))
