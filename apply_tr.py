#!/usr/bin/env python3
"""把译文字典应用到某个英文 .landb 上，输出新的 .landb。

用法: apply_tr.py <英文.landb> <译文字典.py> <输出.landb> [--report]
译文字典是 Python 文件，内含 T = {英文原文: 中文译文}。
"""
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import landb  # noqa: E402


def load_dict(path):
    """载入译文字典；path 可用逗号分隔多个文件，后者覆盖前者。"""
    T = {}
    for p in path.split(','):
        p = p.strip()
        if not p:
            continue
        spec = importlib.util.spec_from_file_location('trmod_%d' % len(T) + os.path.basename(p), p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        T.update(mod.T)
    return T


def load_phrases(dictpath):
    """从字典文件同目录载入可选的 phrases.py（短语级兜底替换）。"""
    d = os.path.dirname(os.path.abspath(dictpath.split(',')[0]))
    p = os.path.join(d, 'phrases.py')
    if not os.path.exists(p):
        return [], ()
    spec = importlib.util.spec_from_file_location('phrases', p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, 'PHRASES', []), getattr(mod, 'KEEP_PREFIXES', ())


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    src, dictpy, dst = sys.argv[1], sys.argv[2], sys.argv[3]
    data = open(src, 'rb').read()
    T = load_dict(dictpy)
    PHRASES, KEEP_PREFIXES = load_phrases(dictpy)
    items = landb.extract(data)
    repl, hit, miss = {}, 0, []
    keep_english = 0
    phrase_fix = 0
    for x in items:
        t = x['text']
        if t in T:
            zh = T[t]
            if zh != t:
                repl[x['off']] = zh
                hit += 1
            else:
                keep_english += 1          # 显式声明「保持英文」
            continue
        # 纯标记条目（去掉 [..] {..} <..> ^..^ 后没有英文字母）→ 视为保留
        stripped = re.sub(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>|\^[^\^]*\^', '', t).strip()
        if not re.search(r'[A-Za-z]', stripped):
            keep_english += 1
            continue
        if KEEP_PREFIXES and t.startswith(tuple(KEEP_PREFIXES)):
            keep_english += 1              # 版权/EULA 等：刻意保留原文
            continue
        # 短语级兜底：逐条替换已知英文短语，保留标记
        nt = t
        for en, zh in PHRASES:
            if en in nt:
                nt = nt.replace(en, zh)
        if nt != t:
            repl[x['off']] = nt
            phrase_fix += 1
        else:
            miss.append(t)
    out, n = landb.rebuild(data, repl)
    open(dst, 'wb').write(out)
    print('%s -> %s' % (os.path.basename(src), os.path.basename(dst)))
    print('  条目 %d：精确译文 %d，短语兜底 %d，声明保留英文 %d，未覆盖 %d，字节 %d -> %d'
          % (len(items), hit, phrase_fix, keep_english, len(miss), len(data), len(out)))
    if miss:
        print('  未覆盖条目（前 40 条）:')
        for t in miss[:40]:
            print('     %r' % t[:90])


if __name__ == '__main__':
    main()
