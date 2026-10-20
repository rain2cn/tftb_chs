#!/usr/bin/env python3
"""通用「应用译文 + 校验」：把 tr 里的合并字典应用到某个英文 .landb，输出到 _work/zh/，并核对标记/中文/制表符。
用法: apply_one.py <归档.ttarch2> <英文文件名或子串> [输出目录=_work/zh]
"""
import importlib.util, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import landb, makedict
import apply_tr as A

# 超长文本块（演职员表巨块，单条 2~3 万字符、上千行）：
#   把它翻成中文会得到「一条 2.8 万字的 CJK 字符串」，引擎逐字排版/换行是 O(n^2) 量级，
#   实测会导致「切换场景载入从数秒变成 1 分钟」。原汉化作者的处理就是**保留英文原文**，这里照做。
#   （见 诊断包/怎么测.txt 的定位记录）
LONG_KEEP = 3000

# 整份资料「不翻译、原样用英文原档」的资源：演职员表（ui_credits*）。
#   理由：整页都是姓名/职务清单，翻成中文收益极低，却会带来超长 CJK 字符串、
#   以及错位/串行等风险。这里直接**逐字节沿用英文原档**，最稳。
#   （对应的 tr 条目不保留、不记载）
SKIP_AS_EN = ('ui_credits',)


def main():
    arch, pat = sys.argv[1], sys.argv[2]
    outdir = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, '_work', 'zh')
    os.makedirs(outdir, exist_ok=True)
    spec = importlib.util.spec_from_file_location('t', os.path.join(HERE, 'ttce.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    c = m.TTContainer(arch, os.path.join(HERE, 'TTL_Blowfish.h')); a = m.TTARCH2(c)
    for e in a.entries:
        n = a.name(e)
        if pat not in n: continue
        data = a.data(e)
        if any(s in n for s in SKIP_AS_EN):
            dst = os.path.join(outdir, n.replace('_english.landb', '_zh.landb'))
            open(dst, 'wb').write(data)
            try:
                cnt = len(landb.extract(data))
            except ValueError:
                cnt = -1
            print('%-56s 条 %s | 整份保留英文原档（演职员表，不翻译）' % (n, cnt if cnt >= 0 else '?'))
            return
        T = makedict.load()
        PHRASES, KEEP = A.load_phrases(os.path.join(HERE, 'tr', 'x.py'))
        try:
            items = landb.extract(data)
        except ValueError:
            # 少数 .landb 用了别的布局（原汉化包也没译过，例：env_05_credits / ui_creditsclosing /
            # env_nexttimeonbl102）。解析不了就**保持英文原档**，不写 _zh 文件。
            print('%-56s 跳过（该 .landb 布局无法解析，保持英文原档）' % n)
            return
        repl, hit, keep, miss, phr, longkeep = {}, 0, 0, [], 0, 0
        for x in items:
            t = x['text']
            if len(t) > LONG_KEEP:
                longkeep += 1; keep += 1
                continue
            if t in T:
                if T[t] != t: repl[x['off']] = T[t]; hit += 1
                else: keep += 1
                continue
            st = re.sub(r'\[[^\]]*\]|\{[^}]*\}|<[^>]*>|\^[^\^]*\^', '', t).strip()
            if not re.search(r'[A-Za-z]', st): keep += 1; continue
            if KEEP and t.startswith(tuple(KEEP)): keep += 1; continue
            nt = t
            for en, zh in PHRASES:
                if en in nt: nt = nt.replace(en, zh)
            if nt != t: repl[x['off']] = nt; phr += 1
            else: miss.append(t)
        out, _nb = landb.rebuild(data, repl)
        dst = os.path.join(outdir, n.replace('_english.landb', '_zh.landb'))
        open(dst, 'wb').write(out)
        # 校验
        en = landb.extract(data); zh = landb.extract(out)
        pm = re.compile(r'\^(?:color|font|glyphScale|imageScale|imageColor)[^\^]*\^|(?<!\\)<[^>]*>|<<id:\d+>>')
        bad = sum(1 for x, y in zip(en, zh) if pm.findall(x['text']) != pm.findall(y['text']))
        zhc = sum(1 for y in zh if re.search(r'[\u4e00-\u9fff]', y['text']))
        tab = sum(1 for x, y in zip(en, zh) if x['text'].count('\t') != y['text'].count('\t'))
        print('%-56s 条 %d | 精确 %d 短语 %d 保留 %d 超长块保留英文 %d 未覆盖 %d | 标记差异 %d 含中文 %d 制表符差 %d'
              % (n, len(zh), hit, phr, keep, longkeep, len(miss), bad, zhc, tab))
        if miss:
            print('   未覆盖示例:', ' | '.join(repr(t[:70]) for t in miss[:5]))
        return
    print('未找到匹配 %s' % pat, file=sys.stderr)

if __name__ == '__main__':
    main()
