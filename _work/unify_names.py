#!/usr/bin/env python3
# 全章统一：① 中文译名 -> 英文；② 英文专名与中文之间补空格（与既有风格一致）
# 只作用于 tr/ep?_*.py（章节文本），不碰 UI/菜单/Project/Boot 的 tr 文件。
import glob, os, re, sys

DRY = ('--apply' not in sys.argv)

CN2EN = [
    ('潘朵拉', 'Pandora'), ('潘多拉', 'Pandora'),
    ('菲欧娜', 'Fiona'), ('菲奥娜', 'Fiona'),
    ('萨沙', 'Sasha'), ('萨莎', 'Sasha'),
    ('斯考特', 'Scooter'), ('斯库特', 'Scooter'),
    ('赫利奥斯', 'Helios'), ('赫利俄斯', 'Helios'),
    ('亥伯龙', 'Hyperion'), ('海伯龙', 'Hyperion'), ('海力昂', 'Hyperion'),
    ('菲利克斯', 'Felix'), ('费利克斯', 'Felix'),
    ('维洛里', 'Vallory'), ('瓦洛里', 'Vallory'),
    ('瑞斯', 'Rhys'), ('沃恩', 'Vaughn'), ('奥古斯特', 'August'),
    ('雅典娜', 'Athena'), ('克罗格', 'Kroger'), ('芬奇', 'Finch'),
    ('莫西', 'Moxxi'), ('马库斯', 'Marcus'),
]

# 需要与中文之间保持一个空格的英文专名（只补空格，不改动字母）
LATIN = ['Pandora', 'Rhys', 'Fiona', 'Sasha', 'Vaughn', 'Scooter', 'Helios', 'Hyperion',
         'August', 'Athena', 'Felix', 'Kroger', 'Finch', 'Moxxi', 'Marcus', 'Vallory',
         'Jack', 'Gortys', 'Loader Bot', 'Loaderbot', 'Claptrap', 'Zer0', 'Cassius',
         'Pollux', 'Vasquez', 'Yvette', 'Springs', 'Nakayama', 'Bossanova', 'Shade',
         'Bigby', 'Hobbs', 'Janey', 'Hatch', 'Dahl', 'Jakobs', 'Maliwan', 'Torgue',
         'Opportunity', 'Hollow Point', 'Old Haven']
LATIN.sort(key=len, reverse=True)

CJK = re.compile(r'[\u4e00-\u9fff]')


def is_cjk(ch):
    return bool(ch) and bool(CJK.match(ch))


def rep_with_space(s, a, b):
    """把 a 换成 b；若相邻是汉字则补一个空格。"""
    out = []
    i = 0
    while True:
        j = s.find(a, i)
        if j < 0:
            out.append(s[i:]); break
        left = s[j - 1] if j > 0 else ''
        right = s[j + len(a)] if j + len(a) < len(s) else ''
        pre = ' ' if is_cjk(left) else ''
        post = ' ' if is_cjk(right) else ''
        out.append(s[i:j]); out.append(pre + b + post)
        i = j + len(a)
    return ''.join(out)


def space_latin(s, name):
    """英文专名两侧若紧贴汉字，补空格。"""
    s = re.sub(r'(?<=[\u4e00-\u9fff])' + re.escape(name), ' ' + name, s)
    s = re.sub(re.escape(name) + r'(?=[\u4e00-\u9fff])', name + ' ', s)
    return s


grand = {}
for p in sorted(glob.glob('tr/ep?_*.py')) + sorted(glob.glob('tr/ep??_*.py')):
    s = open(p, encoding='utf-8').read()
    orig = s
    s = s.replace('帅杰克', '\x00HJ\x00')
    for a, b in CN2EN:
        if a in s:
            grand[a] = grand.get(a, 0) + s.count(a)
            s = rep_with_space(s, a, b)
    n = len(re.findall('杰克', s))
    if n:
        grand['杰克'] = grand.get('杰克', 0) + n
        s = rep_with_space(s, '杰克', 'Jack')
    s = s.replace('\x00HJ\x00', '帅杰克')
    for nm in LATIN:
        s = space_latin(s, nm)
    if s != orig:
        grand.setdefault('__files__', 0)
        grand['__files__'] += 1
        if not DRY:
            open(p, 'w', encoding='utf-8').write(s)

print(('【试运行】' if DRY else '【已应用】') + ' 受影响文件 %d 个' % grand.get('__files__', 0))
for k, v in sorted((k, v) for k, v in grand.items() if k != '__files__'):
    print('  %-8s %d' % (k, v) if not k[0].isascii() else '  %-8s %d' % (k, v))
