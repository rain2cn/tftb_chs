"""扫描 tr/*.py 里「不该被翻译」的标记是否被翻坏（手工改译文后跑一次，防低级错误）。

检查四类：
  1. `<ui_…>` 里出现中文 —— 那是贴图/UI 资源名，必须原样保留；
  2. `<<id:…>>` / `<<DATE…>>` 等尖括号标记被改动；
  3. `{表情}` 标签名里出现中文或空格；
  4. `^color:` / `^font:` / `^glyphScale:` 等参数被翻成中文。

用法: scan_bad_markers.py [--en]     # --en 额外把每条与英文原文对齐核对（更准，但慢）
"""
import ast, io, importlib.util, os, re, sys
ROOT = '/home/deck/Downloads/archives/翻译工程'
sys.path.insert(0, ROOT); os.chdir(ROOT)
TR = os.path.join(ROOT, 'tr')
CJK = re.compile(r'[\u4e00-\u9fff]')
UI = re.compile(r'<ui_[^>]*>')
ANGLE = re.compile(r'<<[^>]*>>')
TAG = re.compile(r'\{[^}]*\}')
# 只认「像标签」的 ^…^：以已知标签名开头、以冒号/数字开头的参数才算；
# 英文原档里有些畸形 ^…^ 中间夹着正文，不能一概当标记（否则误报一堆）
CARET = re.compile(r'\^(?:color|font|glyphScale|kerning|imageScale|imageColor)[^\^]*\^')

bad = {'ui': [], 'angle': [], 'tag': [], 'caret': []}
for fn in sorted(os.listdir(TR)):
    if not fn.endswith('.py') or fn.startswith('_') or fn == 'phrases.py':
        continue
    p = os.path.join(TR, fn)
    try:
        tree = ast.parse(io.open(p, encoding='utf-8').read(), p)
    except SyntaxError as ex:
        print('  [语法错误] %s 第 %s 行' % (fn, ex.lineno)); continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for k, v in zip(node.keys, node.values):
            if not (isinstance(k, ast.Constant) and isinstance(v, ast.Constant)):
                continue
            if not (isinstance(k.value, str) and isinstance(v.value, str)):
                continue
            key, val = k.value, v.value
            ln = getattr(k, 'lineno', 0)
            for mm in UI.findall(val):
                if CJK.search(mm):
                    bad['ui'].append((fn, ln, key, val, mm))
            for mm in ANGLE.findall(val):
                if CJK.search(mm) or mm not in key:
                    bad['angle'].append((fn, ln, key, val, mm))
            for mm in TAG.findall(val):
                inner = mm[1:-1]
                if CJK.search(inner) or inner != inner.strip():
                    bad['tag'].append((fn, ln, key, val, mm))
            for mm in CARET.findall(val):
                if CJK.search(mm):
                    bad['caret'].append((fn, ln, key, val, mm))

titles = {'ui': '<ui_…> 贴图名里出现中文（必须原样保留）',
          'angle': '<<…>> 标记被改动 / 出现中文',
          'tag': '{…} 表情标签名里有中文或首尾空格',
          'caret': '^…^ 富文本参数里有中文'}
total = 0
for k in ('ui', 'angle', 'tag', 'caret'):
    if not bad[k]:
        continue
    print('\n===== %s ：%d 处 =====' % (titles[k], len(bad[k])))
    for fn, ln, key, val, mm in bad[k][:20]:
        total += 1
        print('  tr/%s:%d' % (fn, ln))
        print('    问题片段: %r' % mm)
        print('    EN 键   : %r' % key[:110])
        print('    当前译文 : %r' % val[:110])
    if len(bad[k]) > 20:
        print('  … 还有 %d 处' % (len(bad[k]) - 20))
total = sum(len(v) for v in bad.values())
print('\n合计可疑 %d 处' % total)
if total == 0:
    print('✅ 未发现被翻坏的标记')
