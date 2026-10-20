#!/usr/bin/env python3
"""
TFTB (Tales from the Borderlands) 字体工具  —— 命令行入口

用法:
  python3 tftb.py list    <archive.ttarch2>              列出归档内文件
  python3 tftb.py extract <archive.ttarch2> <输出目录>    解包（自动解密 TTCE）
  python3 tftb.py pack    <输入目录> <输出.ttarch2>        重新打包（自动加密+压缩）
  python3 tftb.py atlas   <某个.font> <输出前缀>           把字形图集解码成 PNG
  python3 tftb.py vf      <字体.ttf>                      列出可变字体(VF)的轴与命名实例

换字体请用 run_all.py（可配合 --vf 指定字重/实例）。

依赖同目录的 ttce.py、atlas.py、TTL_Blowfish.h、Borderlands_key.bin
（TTL_Blowfish.h 来自 Lucas Saragosa 的 TelltaleToolLib，含 Blowfish 常量表与各游戏密钥）
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import ttce  # noqa: E402

CONST = os.path.join(HERE, 'TTL_Blowfish.h')


def _key():
    p = os.path.join(HERE, 'Borderlands_key.bin')
    return open(p, 'rb').read() if os.path.exists(p) else ttce.load_game_key(CONST)


def cmd_list(path, pattern=None):
    c = ttce.TTContainer(path, CONST)
    a = ttce.TTARCH2(c)
    print('%s  页数=%d  窗口=%d  归档大小=%d' % (os.path.basename(path), c.num_pages, c.window, c.page_off[-1]))
    total = 0
    for e in a.entries:
        n = a.name(e)
        total += e['size']
        if pattern and pattern.lower() not in n.lower():
            continue
        print('  %10d  %s' % (e['size'], n))
    print('  ---- 共 %d 个资源，解压后 %.1f MB' % (a.count, total / 1048576))


def cmd_extract(path, outdir):
    c = ttce.TTContainer(path, CONST)
    a = ttce.TTARCH2(c)
    os.makedirs(outdir, exist_ok=True)
    for e in a.entries:
        n = a.name(e)
        p = os.path.join(outdir, n.replace('\\', '/'))
        d = os.path.dirname(p)
        if d:
            os.makedirs(d, exist_ok=True)
        open(p, 'wb').write(a.data(e))
        print('  写出 %10d  %s' % (e['size'], n))


def cmd_pack(indir, outpath):
    files = []
    for root, _, names in os.walk(indir):
        for n in names:
            fp = os.path.join(root, n)
            rel = os.path.relpath(fp, indir).replace(os.sep, '/')
            files.append((rel, open(fp, 'rb').read()))
    bfp, ks = ttce.load_constants(CONST)
    ttce.pack_ttarch2(files, outpath, bfp, ks, _key(),
                      log=lambda m: print('  ' + m))


def cmd_atlas(fontpath, outprefix):
    import atlas
    d = open(fontpath, 'rb').read()
    size = None
    for p in (24, 23, 22, 21, 20):
        if len(d) > (1 << p):
            size = 1 << p
            break
    tex = d[len(d) - size:]
    print('图集大小 %d；候选尺寸：%s' % (size, [w for w in (1024, 2048, 512, 4096) if size % w == 0]))
    for (w, h) in [(1024, 2048), (2048, 1024), (4096, 4096), (2048, 4096), (512, 4096), (1024, 4096)]:
        if w * h != size:
            continue
        a = atlas.bc3_alpha(tex, w, h)
        atlas.write_png_gray('%s_alpha_%dx%d.png' % (outprefix, w, h), w, h, a)
        r = atlas.bc1_rgb(tex, w, h)
        atlas.write_png_gray('%s_rgb_%dx%d.png' % (outprefix, w, h), w, h, r)
        print('  已写出 %s_alpha_%dx%d.png / %s_rgb_%dx%d.png' % (outprefix, w, h, outprefix, w, h))


def cmd_vf(ttfpath):
    """列出字体信息：是否可变字体、有哪些轴、有哪些命名实例（供 --vf / --vf-name 使用）。"""
    import rebake
    axes, inst = rebake.font_variation_info(ttfpath)
    print('字体: %s' % ttfpath)
    if not axes:
        try:
            import PIL  # noqa: F401
            print('  不是可变字体（没有 fvar 表）——直接渲染即可，无需 --vf')
        except Exception:
            print('  读不到字体信息：本脚本需要 Pillow/fontTools，请用目录内的虚拟环境运行，例如')
            print('    .venv/bin/python tftb.py vf %s' % ttfpath)
        return
    print('  可变轴:')
    for a in axes:
        print('    %-6s %-10s  min=%g  default=%g  max=%g'
              % (a['tag'], a['name'], a['min'], a['default'], a['max']))
    print('  命名实例（可直接 --vf-name 使用）:')
    for i in inst:
        print('    %-16s %s' % (i['name'], ', '.join('%s=%g' % (k, v) for k, v in i['coords'].items())))
    print('  用法示例: --vf "wght=400"   或   --vf-name "Regular-Round"')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    table = {'list': cmd_list, 'extract': cmd_extract, 'pack': cmd_pack,
             'atlas': cmd_atlas, 'vf': cmd_vf}
    if cmd not in table:
        print(__doc__)
        sys.exit(1)
    table[cmd](*args)
