t=[*input()]
z=t.pop
E=lambda:([z(0),z(0),z(0)][1],E())if t[0]=="λ"else(lambda x:x if t[0]==")"else[x,A()])(A())
A=lambda:(m:=z(0))and([E(),z(0)][0]if m=="("else m)
Z=lambda*_,**k:lambda x,e=0:eval(k[str(type(x))[8]])
F=Z(t='f"(λ{x[0]}.{F(x[1])})"',l='"("+F(x[0])+F(x[1])+")"',s='x')
R=Z(l='(f:=R(x[0],e),R(f[1],e|{f[0]:R(x[1],e)}))[1]',t="x",s="e[x]")
x=E()
while(y:=R(x,{}))!=x:x=y
print(F(x))
