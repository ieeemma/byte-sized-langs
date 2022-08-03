i=__import__
t=i('re').findall(r'\(|\)|[^\s\(\)]+',f'({i("sys").stdin.read()})')
L=lambda:t.pop(0)and[]if t[0]==')'else[S(),L()]
S=lambda:(x:=t.pop(0))and(L()if x=='('else int(x)if x.isdigit()else x)
T=lambda l:[l[0]]+T(l[1])if l else[]
F=lambda l:[l[0],F(l[1:])]if l else[]
X=type
M=lambda p,a:(z:=[*zip(p,a)])and M(*z[1])|dict([z[0]])if p else{}
def E(x,e):
 if X(x)!=list:return e[x]if X(x)==str else x
 f=E(x[0],e);m=f[0]=='!';f=f[m:];a=x[1]if m else F([E(y,e)for y in T(x[1])])
 return eval(f,globals()|{'A':a}|M(F('eabc'[:len(T(a))+1]),[e,a]))if X(f)==str else E(f[1],e|M(f[0],a))
def I(a,b,c):a[b]=c
V={'quote':'!a','=':'!I(e,a,E(b,e))','lambda':'![a,b]','if':'!E([b,c][not E(a,e)],e)','let':'!E(c,e|{a:E(b,e)})','do':'T(A)[-1]','cons':'[a,b]','car':'a[0]','cdr':'a[1]','car=':'I(a,0,b)','cdr=':'I(a,1,b)','list':'A','+':'a+b','-':'a-b','*':'a*b','/':'a/b','==':'a==b','&':'a and b','|':'a or b','print':'print(a)','exit':'exit(a)','t?':'X(a).__name__==b',}
for e in T(S()):E(e,V)
