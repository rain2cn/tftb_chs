import re, sys, ast
CJK=r'[\u4e00-\u9fff\u3000-\u303f\uff01-\uff65]'
def fix(path):
    lines=open(path,encoding='utf-8').read().split('\n')
    out=[]
    for ln in lines:
        if ln.lstrip().startswith('#'):
            out.append(ln); continue
        n=len(ln)
        # 标记定界引号位置
        delim=set()
        for m in re.finditer(r'"', ln):
            i=m.start()
            prev=ln[i-1] if i>0 else ''
            nxt=ln[i+1] if i+1<n else ''
            if i==ln.index(ln.lstrip()) if ln.strip() else False: pass
            if re.match(r'^\s*$', ln[:i]): delim.add(i)          # 行首（缩进后）
            elif prev==':' and i>=2 and ln[i-2]==' ': delim.add(i)  # 值开头
            elif prev==' ' and i>=2 and ln[i-2]==':': delim.add(i)  # 值开头(单空格也覆盖)
            elif nxt in ',:' : delim.add(i)                        # 值/键结尾
        pos=[m.start() for m in re.finditer(r'"', ln) if m.start() not in delim
             and ((m.start()>0 and re.match(CJK, ln[m.start()-1])) or (m.start()+1<n and re.match(CJK, ln[m.start()+1])))]
        if pos:
            ch=list(ln)
            for k,i in enumerate(pos):
                ch[i]='“' if k%2==0 else '”'
            ln=''.join(ch)
        out.append(ln)
    s='\n'.join(out)
    open(path,'w',encoding='utf-8').write(s)
    try:
        ast.parse(s); print("语法 OK，文件 %d 字符"%len(s))
    except SyntaxError as e:
        print("语法错误 line",e.lineno,repr(e.text))
if __name__=='__main__':
    fix(sys.argv[1])
