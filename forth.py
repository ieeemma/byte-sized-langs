i=__import__
X=type
t=i("re").findall("{|}|[^\s{}]+",i("sys").stdin.read())
z=t.pop
p=t.extend
e={"dup":"p((α,α))","pop":"()#α","swap":"p((β,α))","if":"[*map(E,[β,γ][not α])]and()","=":"e.__setitem__(β[0],(α,))",'+':'α+β','-':'α-β','*':'α*β','/':'α/β','==':'α==β',"print":"print(α)","exit":"exit"}
P=lambda:(m:=z(0))and(L(())if m=="{"else m.isdigit()and int(m)or m)
L=lambda x:z(0)and x if t[0]=="}"else L(x+(P(),))
def E(x):([*map(E,f)]if(f:=e[x])and X(f)==X(())else((r:=eval(f,globals()|{c:z()for c in"γβα"if f.count(c)}))==0 or r)and p([r]))if x in e else p([x])
while t and(n:=z(0)):e[n]=P()
E("main")
