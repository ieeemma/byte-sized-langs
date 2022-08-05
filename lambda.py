t=[*input()]
z=t.pop
E=lambda:([z(0),z(0),z(0)][1],E())if t[0]=="λ"else(lambda x:x if t and t[0]==")"else[x,A()])(A())
A=lambda:(m:=z(0),E(),z(0))[1]if m=="("else m)
Z=lambda*_,**k:lambda x,*y:eval(k[str(type(x))[8]])
F=Z(t='f"(λ{x[0]}.{F(x[1],0)})"',l='(o:=F(x[0],0)+F(x[1],1))and[o,f"({o})"][y[0]]',s='x')
R=Z(l='(e:=y[0],f:=R(x[0],e),R(f[1],e|{f[0]:R(x[1],e)}))[2]',t="x",s="y[0][x]")
x=E()
while(y:=R(x,{}))!=x:x=y
print(F(x,0))
