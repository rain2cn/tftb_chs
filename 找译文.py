#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""找译文：给定一段**中文**（或英文原文片段），告诉你要改哪个文件、哪一行，以及改完该重建哪个归档。

用法:
    找译文.py "打完收工"              # 按中文查找
    找译文.py -e "Catch a Ride"       # 按英文原文查找（-e / --en）
    找译文.py "Gortys" --all          # 显示全部命中（默认最多 20 条）

输出包含三段：
  1) 命中的 tr 文件 + 行号 + 键/值
  2) 这个「键」出现在哪些归档 / 哪个资源里  -> 决定要重建哪个归档
  3) 一键重建的命令
"""
import ast
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(ROOT, 'tr')
EN_DIR = os.path.join(ROOT, '..', '原版英文档')
ARCH_BY_FILE = {
    'Project': 'Project', 'Menu': 'Menu', 'Boot': 'Boot',
    'Borderlands101': 'Borderlands101', 'Borderlands102': 'Borderlands102',
    'Borderlands103': 'Borderlands103', 'Borderlands104': 'Borderlands104',
    'Borderlands105': 'Borderlands105',
}


def load_tr():
    """返回 [(文件, 行号, 键, 值)]，按文件、行号排序。"""
    out = []
    for fn in sorted(os.listdir(TR)):
        if not fn.endswith('.py') or fn.startswith('_'):
            continue
        p = os.path.join(TR, fn)
        try:
            tree = ast.parse(open(p, encoding='utf-8').read(), p)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue
            for k, v in zip(node.keys, node.values):
                if isinstance(k, ast.Constant) and isinstance(v, ast.Constant) \
                        and isinstance(k.value, str) and isinstance(v.value, str):
                    out.append((fn, getattr(k, 'lineno', 0), k.value, v.value))
    return out


def find_archives(keys, log=print):
    """扫描原版归档，返回 {键: [(归档, 资源名)]}。"""
    spec = importlib.util.spec_from_file_location('t', os.path.join(ROOT, 'ttce.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    import landb
    want = set(keys)
    hit = {k: [] for k in keys}
    for fn in sorted(os.listdir(EN_DIR)):
        if not fn.endswith('.ttarch2'):
            continue
        tag = fn.replace('Borderlands_pc_', '').replace('_data.ttarch2', '')
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
            got = set(x['text'] for x in S) & want
            for k in got:
                hit[k].append((tag, n))
            del S
    return hit


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        return 1
    by_en = False
    show_all = False
    pat = None
    for a in argv:
        if a in ('-e', '--en'):
            by_en = True
        elif a == '--all':
            show_all = True
        else:
            pat = a
    if not pat:
        print(__doc__)
        return 1

    rows = load_tr()
    hits = []
    for fn, ln, k, v in rows:
        target = k if by_en else v
        if pat in target:
            hits.append((fn, ln, k, v))
    print('译文键共 %d 个（来自 %d 个文件）' % (len(rows), len(set(r[0] for r in rows))))
    print('匹配 %r（按%s）：命中 %d 处\n' % (pat, '英文原文' if by_en else '中文译文', len(hits)))
    if not hits:
        print('没有命中。换个片段试试（注意：超长演职员表块按约定保留英文，不在译文里）。')
        return 0
    limit = len(hits) if show_all else 20
    for fn, ln, k, v in hits[:limit]:
        print('  📄 tr/%s  第 %d 行' % (fn, ln))
        print('     EN 键 : %r' % (k[:110]))
        print('     ZH 值 : %r' % (v[:110]))
    if len(hits) > limit:
        print('  … 还有 %d 处（加 --all 全部显示）' % (len(hits) - limit))

    keys = list(dict.fromkeys(k for _, _, k, _ in hits))
    print('\n正在核对这些键出现在哪些归档 …')
    hit = find_archives(keys)
    tags = []
    for k in keys:
        for tag, res in hit.get(k, []):
            print('  %-15s %s' % (tag, res))
            if tag in ARCH_BY_FILE and tag not in tags:
                tags.append(tag)
    print()
    if tags:
        print('✅ 改完请重建这些归档：')
        print('   cd %s' % ROOT)
        print('   .venv/bin/python 一键重建.py %s' % ' '.join(tags))
    else:
        print('⚠️ 这些键在原版归档里找不到（可能是孤儿键/历史遗留），改它不会生效。')
    print('\n改完建议再跑一次：.venv/bin/python _work/key_integrity.py')
    return 0


if __name__ == '__main__':
    sys.exit(main())
