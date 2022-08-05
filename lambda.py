t=[*input()]
z=t.pop
T=type
class Q(tuple):...
E=lambda:([z(0),z(0),z(0)][1],E())if t[0]=="λ"else(lambda x:x if t and t[0]==")"else Q([x,A()]))(A())
A=lambda:(m:=z(0))and([E(),z(0)][0]if m=="("else m)
F=lambda x,p:f"(λ{x[0]}.{F(x[1],0)})"if T(x)==tuple else((o:=F(x[0],0)+" "+F(x[1],1))and[o,f"({o})"][p])if T(x)==Q else x
R=lambda x,e:(f:=R(x[0],e))and R(f[1],e|{f[0]:R(x[1],e)})if T(x)==Q else e.get(x,x)
x=E()
while (y:=R(x,{}))!=x:x=y
print(F(x,0))
