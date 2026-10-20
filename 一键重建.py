#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一键重建全部汉化归档 —— 改完 tr/*.py 里的译文后运行本脚本即可。

**不依赖任何第三方汉化包/基底目录**：来源只有「原版英文档」+ `tr/`。

流程（对每个归档）：
  1. 把 tr/*.py 合并出的字典套用到「原版英文档」对应的 *_english.landb；
  2. 只把**与英文原文不同**的那些资源打进一个「覆盖包」（ttarch2），
     输出命名为 `Borderlands_pc_chs_full_<归档名>.ttarch2`（与 resdesc lua 指向的名字一致）；
  3. 逐条核验 未覆盖 / 标记差异 / 制表符差，三项必须全为 0，否则报错并非零退出。

用法：
    python3 一键重建.py               # 重建全部 8 个归档
    python3 一键重建.py Menu          # 只重建指定归档（可写多个：Menu Borderlands105）
    python3 一键重建.py --list        # 列出可用的归档名
    python3 一键重建.py --check       # 只核验现有产物，不重建

前置：译文写在 tr/<...>_zh.py，格式为字典 `T = {"英文": "中文", ...}` 或 `T.update({...})`。
      键必须与原文逐字节一致；原文换行写 `\\n`（不是 `\\\\n`），制表符写 `\\t`。
"""
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
EN_DIR = os.path.join(HERE, '..', '原版英文档')        # 唯一来源：原版英文归档
OUT_DIR = os.path.join(HERE, '..', '汉化成品')         # 成品输出（覆盖包）
ZHDIR = os.path.join(HERE, '_work', 'zh')              # 中间：套用后的 _zh.landb

# 归档名 -> 原版英文归档文件名
TARGETS = [
    ('Project', 'Borderlands_pc_Project_data.ttarch2'),
    ('Menu', 'Borderlands_pc_Menu_data.ttarch2'),
    ('Boot', 'Borderlands_pc_Boot_data.ttarch2'),
    ('Borderlands101', 'Borderlands_pc_Borderlands101_data.ttarch2'),
    ('Borderlands102', 'Borderlands_pc_Borderlands102_data.ttarch2'),
    ('Borderlands103', 'Borderlands_pc_Borderlands103_data.ttarch2'),
    ('Borderlands104', 'Borderlands_pc_Borderlands104_data.ttarch2'),
    ('Borderlands105', 'Borderlands_pc_Borderlands105_data.ttarch2'),
]

PM = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>')

# 非 landb 的补丁资源（归档名 -> [(资源名, 文件路径)]）。
# 目前只有一处：UI_data 里 ui_notification.scene 的「开发占位乱码」，
# 它不在任何 .landb 里（原汉化包也翻不了），只能等长替换后挂到某个已挂载的覆盖包里。
EXTRA_RES = {
    'Project': [('ui_notification.scene', os.path.join(HERE, '_work', 'scene', 'ui_notification.scene'))],
    'Menu':    [('ui_notification.scene', os.path.join(HERE, '_work', 'scene', 'ui_notification.scene'))],
}


def _m():
    spec = importlib.util.spec_from_file_location('t', os.path.join(HERE, 'ttce.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def english_names(arch_path):
    """列出归档里的 *_english.landb 资源名。"""
    m = _m()
    c = m.TTContainer(arch_path, os.path.join(HERE, 'TTL_Blowfish.h'))
    a = m.TTARCH2(c)
    return [a.name(e) for e in a.entries if a.name(e).endswith('_english.landb')]


def drop_zh(name):
    """清掉某资源可能残留的旧 _zh 文件（单文件删除）。"""
    p = os.path.join(ZHDIR, name.replace('_english.landb', '_zh.landb'))
    try:
        if os.path.exists(p):
            os.remove(p)
    except OSError:
        pass


def apply_one(en_arch, name):
    """套用字典并返回 apply_one 的统计行文本。"""
    r = subprocess.run([PY, os.path.join(HERE, 'apply_one.py'), en_arch, name, ZHDIR],
                       capture_output=True, text=True)
    return (r.stdout or '').strip(), (r.stderr or '').strip()


def parse_stats(line):
    d = {}
    for key in ('未覆盖', '标记差异', '制表符差', '超长块保留英文'):
        m = re.search(re.escape(key) + r'\s*(\d+)', line)
        d[key] = int(m.group(1)) if m else None
    return d


def check_archive(zh_path, en_path):
    """核验产物：只统计覆盖包里真正替换掉的资源；标记/制表符必须一致。
    内存友好：按需解包，逐一比对。"""
    import gc
    import landb
    m = _m()
    c_en = m.TTContainer(en_path, os.path.join(HERE, 'TTL_Blowfish.h'))
    a_en = m.TTARCH2(c_en)
    en_entry = {}
    for e in a_en.entries:
        n = a_en.name(e)
        if n.endswith('_english.landb'):
            en_entry[n] = e
    c_zh = m.TTContainer(zh_path, os.path.join(HERE, 'TTL_Blowfish.h'))
    a_zh = m.TTARCH2(c_zh)
    tot = zhc = bad = tab = 0
    for e in a_zh.entries:
        n = a_zh.name(e)
        if n not in en_entry:
            continue
        try:
            x = landb.extract(a_en.data(en_entry[n]))
            y = landb.extract(a_zh.data(e))
        except ValueError:
            continue
        if len(x) != len(y):
            return None
        for u, v in zip(x, y):
            tot += 1
            if re.search(r'[\u4e00-\u9fff]', v['text']):
                zhc += 1
            if PM.findall(u['text']) != PM.findall(v['text']):
                bad += 1
            if u['text'].count('\t') != v['text'].count('\t'):
                tab += 1
        del x, y
        gc.collect()
    return tot, zhc, bad, tab


def main():
    argv = [a for a in sys.argv[1:]]
    if '--list' in argv or '-l' in argv:
        print('可用归档名：' + '  '.join(t[0] for t in TARGETS))
        return 0
    only_check = '--check' in argv
    pick = [a for a in argv if not a.startswith('-')]

    # 父模式：未指定归档 → 每个归档起一个子进程，避免内存累积（大归档一次做完会 OOM）
    if not pick:
        print('=' * 78)
        print('一键重建 —— 共 %d 个归档%s（只依赖 原版英文档/ + tr/）'
              % (len(TARGETS), '（仅核验）' if only_check else ''))
        print('=' * 78)
        fails = []
        for name, _ in TARGETS:
            cmd = [PY, os.path.abspath(__file__), name] + (['--check'] if only_check else [])
            if subprocess.run(cmd).returncode != 0:
                fails.append(name)
        print('\n' + '=' * 78)
        if fails:
            print('❌ 有 %d 个归档未通过：%s' % (len(fails), '  '.join(fails)))
            return 1
        print('✅ 全部 %d 个归档均已重建并核验通过（未覆盖 0 / 标记差异 0 / 制表符差 0）' % len(TARGETS))
        print('   产物目录：%s' % os.path.normpath(OUT_DIR))
        return 0

    targets = [t for t in TARGETS if t[0] in pick]
    if not targets:
        print('未知归档名：%s（用 --list 查看）' % ' '.join(pick))
        return 2

    print('=' * 78)
    print('一键重建 —— 共 %d 个归档' % len(targets) + ('（仅核验）' if only_check else ''))
    print('=' * 78)

    problems = []
    summary = []
    for name, en_file in targets:
        en = os.path.join(EN_DIR, en_file)
        if not os.path.exists(en):
            problems.append('%s：找不到英文档 %s' % (name, en))
            continue
        out_path = os.path.join(OUT_DIR, 'Borderlands_pc_chs_full_%s.ttarch2' % name)
        names = english_names(en)
        print('\n【%s】%d 个文本资源' % (name, len(names)))

        if not only_check:
            os.makedirs(ZHDIR, exist_ok=True)
            pairs, skipped, skipped_unparsable = [], 0, 0
            m = _m()
            import landb
            c_en = m.TTContainer(en, os.path.join(HERE, 'TTL_Blowfish.h'))
            a_en = m.TTARCH2(c_en)
            for e in a_en.entries:
                n = a_en.name(e)
                if not n.endswith('_english.landb'):
                    continue
                out, err = apply_one(en, n)
                if not out or '未找到匹配' in out or err:
                    problems.append('%s / %s：套用失败 %s%s' % (name, n, out[:80], err[:120]))
                    print('   ✗ %s 套用失败' % n)
                    drop_zh(n)
                    continue
                if '跳过' in out and '无法解析' in out:
                    drop_zh(n)
                    skipped_unparsable += 1
                    print('   · %s  （布局无法解析，保持英文原档）' % n)
                    continue
                st = parse_stats(out)
                flag = ''
                if st['未覆盖']:
                    flag = '  ⚠ 未覆盖 %d 条' % st['未覆盖']
                    problems.append('%s / %s：未覆盖 %d 条' % (name, n, st['未覆盖']))
                if st.get('超长块保留英文'):
                    flag += '  （超长块保留英文 %d）' % st['超长块保留英文']
                zh_file = os.path.join(ZHDIR, n.replace('_english.landb', '_zh.landb'))
                src = a_en.data(e)
                new = open(zh_file, 'rb').read() if os.path.exists(zh_file) else None
                if new is None:
                    problems.append('%s / %s：没有产出 _zh 文件' % (name, n))
                    continue
                if new == src:            # 与英文原文一致 → 不必进覆盖包
                    skipped += 1
                    print('   · %s%s  （与英文原文相同，不进覆盖包）' % (n, flag))
                else:
                    pairs.append('%s=%s' % (n, zh_file))
                    print('   · %s%s' % (n, flag))
                if st['标记差异'] or st['制表符差']:
                    problems.append('%s / %s：标记差异 %s / 制表符差 %s'
                                    % (name, n, st['标记差异'], st['制表符差']))
            if not pairs:
                problems.append('%s：没有任何需要覆盖的资源' % name)
                print('   ✗ 没有任何需要覆盖的资源')
                continue
            for rname, rpath in EXTRA_RES.get(name, []):
                if os.path.exists(rpath):
                    pairs.append('%s=%s' % (rname, rpath))
                    print('   + %s（非文本补丁资源）' % rname)
                else:
                    problems.append('%s：缺少补丁资源 %s' % (name, rpath))
            r = subprocess.run([PY, os.path.join(HERE, 'build_overlay.py'), out_path] + pairs,
                               capture_output=True, text=True)
            for ln in (r.stdout or '').splitlines():
                print('   ' + ln.strip())
            if r.returncode != 0 or '全部一致' not in (r.stdout or ''):
                problems.append('%s：装配失败 %s' % (name, (r.stderr or '')[-200:]))
                print('   ✗ 装配失败')
                continue
            print('   （%d 个资源与英文原文相同 / %d 个布局无法解析，均未装入覆盖包）'
                  % (skipped, skipped_unparsable))
            sz = os.path.getsize(out_path)
        else:
            if not os.path.exists(out_path):
                problems.append('%s：产物不存在' % name)
                continue
            sz = os.path.getsize(out_path)

        res = check_archive(out_path, en)
        if res is None:
            problems.append('%s：条目数不一致' % name)
            continue
        tot, zhc, bad, tab = res
        summary.append((name, len(names), tot, zhc, bad, tab, sz))
        print('   → 覆盖资源条目 %d | 含中文 %d (%.1f%%) | 标记差异 %d | 制表符差 %d | %d 字节'
              % (tot, zhc, 100.0 * zhc / max(tot, 1), bad, tab, sz))
        if bad or tab:
            problems.append('%s：产物标记差异 %d / 制表符差 %d' % (name, bad, tab))

    print('\n' + '=' * 78)
    if summary:
        print('%-16s %4s %8s %8s %6s %6s' % ('归档', '资源', '条目', '含中文', '标记差', '制表符差'))
        for name, nr, tot, zhc, bad, tab, sz in summary:
            print('%-16s %4d %8d %8d %6d %6d' % (name, nr, tot, zhc, bad, tab))
    if problems:
        print('\n❌ 有 %d 个问题：' % len(problems))
        for p in problems:
            print('   - ' + p)
        return 1
    print('\n✅ 全部完成：%d 个归档均已重建并核验（标记差异 0 / 制表符差 0）' % len(summary))
    print('   产物目录：%s' % os.path.normpath(OUT_DIR))
    return 0


if __name__ == '__main__':
    sys.exit(main())
