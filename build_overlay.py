#!/usr/bin/env python3
"""装配「覆盖包」：把若干 .landb 打进一个新的 ttarch2（不再需要任何第三方汉化包/基底归档）。

用法: build_overlay.py <输出归档路径> <资源名>=<landb 路径> [<资源名>=... ...]

说明：
  · 只装给定的资源，资源名按原样写进名表（引擎按名字查找，会覆盖游戏原有资源）；
  · 不依赖任何基底归档；分页窗口/加密/压缩与游戏一致（ttce.pack_ttarch2）。
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ttce  # noqa: E402

CONST = os.path.join(HERE, 'TTL_Blowfish.h')


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    out = sys.argv[1]
    pairs = []
    for a in sys.argv[2:]:
        name, path = a.split('=', 1)
        pairs.append((name, open(path, 'rb').read()))
    bfp, ks = ttce.load_constants(CONST)
    key = ttce.load_game_key(CONST)
    d = os.path.dirname(out)
    if d:
        os.makedirs(d, exist_ok=True)
    lvl = int(os.environ.get('TTARCH2_LEVEL', '1'))
    ttce.pack_ttarch2(pairs, out, bfp, ks, key, level=lvl)
    print('  打包 %d 个资源 -> %s (%d 字节, level=%d)' % (len(pairs), os.path.basename(out), os.path.getsize(out), lvl))
    # 回读校验
    c2 = ttce.TTContainer(out, CONST)
    a2 = ttce.TTARCH2(c2)
    want = dict(pairs)
    bad = [a2.name(e) for e in a2.entries if a2.data(e) != want.get(a2.name(e))]
    print('  回读校验: %s' % ('全部一致' if not bad and len(a2.entries) == len(pairs) else '有不一致 %r' % bad))
    return 0 if (not bad and len(a2.entries) == len(pairs)) else 1


if __name__ == '__main__':
    sys.exit(main())
