#!/usr/bin/env python3
"""一键流程：解包字体档 -> 用目标 TTF 重绘「指定」.font 的图集 -> 重打包 -> 回读校验

未列入 --only 的字体保持**原版字节不变**（直接搬运）。

用法:
    .venv/bin/python run_all.py [源.ttarch2] [字体.ttf] [输出目录] [只改哪些字体,逗号分隔]
默认:
    源     = ../Borderlands_pc_chs_fonts_v6.ttarch2
    字体   = ../alifangyuan.ttf
    输出   = ../输出_阿里方圆体字体包
    只改   = Rockwell.font          （写 ALL 表示全部 13 个都改）
"""
import os
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ttce          # noqa: E402
import rebake        # noqa: E402

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', 'Borderlands_pc_chs_fonts_v6.ttarch2')
TTF = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, '..', 'alifangyuan.ttf')
OUTDIR = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, '..', '输出_阿里方圆体字体包')
ONLY = [x.strip() for x in (sys.argv[4] if len(sys.argv) > 4 else 'Rockwell.font').split(',') if x.strip()]
if ONLY and ONLY[0].upper() == 'ALL':
    ONLY = None                       # None = 全部重绘
CONST = os.path.join(HERE, 'TTL_Blowfish.h')

t0 = time.time()
tmp_ext = os.path.join(HERE, '_extract')
tmp_rbk = os.path.join(HERE, '_rebake')
for d in (tmp_ext, tmp_rbk):
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)

print('==== 1/4 解包 %s' % os.path.basename(SRC))
c = ttce.TTContainer(SRC, CONST)
a = ttce.TTARCH2(c)
orig = {}
for e in a.entries:
    n = a.name(e)
    d = a.data(e)
    open(os.path.join(tmp_ext, n), 'wb').write(d)
    orig[n] = d
    print('   %10d  %s' % (len(d), n))
print('   解包完成 %.1fs' % (time.time() - t0))

print('==== 2/4 重绘字形图集（目标字体: %s）'
      % ('全部' if ONLY is None else ', '.join(ONLY)))
for n, d in orig.items():
    if ONLY is not None and n not in ONLY:
        open(os.path.join(tmp_rbk, n), 'wb').write(d)          # 原样搬运
        print('   [保持不变] %s' % n)
        continue
    print('== %s' % n)
    out, (W, H), alpha = rebake.rebake_font(d, TTF, log=lambda s: print(s, flush=True))
    assert len(out) == len(d), '长度必须不变'
    open(os.path.join(tmp_rbk, n), 'wb').write(out)
print('   重绘完成 %.1fs' % (time.time() - t0))

print('==== 3/4 重打包')
bfp, ks = ttce.load_constants(CONST)
key = ttce.load_game_key(CONST)
os.makedirs(OUTDIR, exist_ok=True)
outpath = os.path.join(OUTDIR, os.path.basename(SRC))
newfiles = [(n, open(os.path.join(tmp_rbk, n), 'rb').read()) for n in orig]
ttce.pack_ttarch2(newfiles, outpath, bfp, ks, key, level=9, log=lambda s: print('  ' + s))
print('   原包 %d 字节 -> 新包 %d 字节' % (os.path.getsize(SRC), os.path.getsize(outpath)))

print('==== 4/4 校验')
c2 = ttce.TTContainer(outpath, CONST)
a2 = ttce.TTARCH2(c2)
print('   资源数 %d' % a2.count)
allok = True
changed, kept = [], []
for e1, e2 in zip(a.entries, a2.entries):
    n = a.name(e1)
    d2 = a2.data(e2)
    same_as_orig = (d2 == orig[n])
    same_as_new = (d2 == open(os.path.join(tmp_rbk, n), 'rb').read())
    want_change = (ONLY is None) or (n in ONLY)
    ok = same_as_new and (same_as_orig != want_change)
    allok &= ok
    (changed if not same_as_orig else kept).append(n)
    print('   %-28s 与原版%s  %s' % (n, '相同' if same_as_orig else '不同',
                                    'OK' if ok else '不符预期!'))
print('   实际改动: %s' % (', '.join(changed) if changed else '（无）'))
print('   保持不变: %d 个' % len(kept))
print('全部符合预期' if allok else '存在不符预期')
print('成品: %s' % outpath)
print('总耗时 %.1fs' % (time.time() - t0))
