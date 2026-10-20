#!/usr/bin/env python3
"""把 tr/*.py 合并成扁平字典缓存 _work/merged.json。
用 ast 静态解析字面量字典，不执行模块（执行会因互相嵌套导入导致内存爆炸）。
用法: makedict.py   —— 也可被 status.py / todo_lines.py 自动调用。
"""
import ast, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
TR = os.path.join(HERE, 'tr')
CACHE = os.path.join(HERE, '_work', 'merged.json')

def _dicts_from(path):
    """取出文件里所有字面量字典（T = {...} 与 T.update({...})），按出现顺序。"""
    tree = ast.parse(open(path, encoding='utf-8').read(), path)
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict) and all(isinstance(k, ast.Constant) for k in node.keys):
            try:
                out.append(ast.literal_eval(node))
            except (ValueError, SyntaxError):
                pass
    return out

def build(save=True):
    T = {}
    for f in sorted(os.listdir(TR)):
        if f.endswith('.py') and not f.startswith('_') and f != 'phrases.py':
            try:
                for d in _dicts_from(os.path.join(TR, f)):
                    T.update(d)
            except SyntaxError as e:
                print('  [警告] 跳过语法有误的 tr/%s（第 %s 行）' % (f, e.lineno), file=sys.stderr)
    if save:
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        json.dump(T, open(CACHE, 'w', encoding='utf-8'), ensure_ascii=False)
    return T

def newest_src():
    n = 0
    for f in os.listdir(TR):
        if f.endswith('.py'):
            n = max(n, os.path.getmtime(os.path.join(TR, f)))
    return n

def load():
    if os.path.exists(CACHE) and os.path.getmtime(CACHE) >= newest_src():
        return json.load(open(CACHE, encoding='utf-8'))
    return build()

if __name__ == '__main__':
    T = load()
    print('合并键数 %d -> %s' % (len(T), CACHE))
