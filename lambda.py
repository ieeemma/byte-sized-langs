t=__import__('re').findall(r'[().λ]|[a-z]+',"(λx. x)(λx. x)")
z=t.pop
T=type
E=lambda:([z(0),z(0),z(0)][1],E())if t[0]=="λ"else(lambda x:x if t and t[0]==")"else[x,A()])(A())
A=lambda:(m:=z(0))and([E(),z(0)][0]if m=="("else m)
R=lambda x,e:R(x[0][1],e|{x[0][0]:x[1]})if type(x)==list else e.get(x,x)
F=lambda x,p:f"(λ{x[0]}. {F(x[1],0)})"if T(x)==tuple else((o:=F(x[0],0)+" "+F(x[1],1))and[o,f"({o})"][p])if T(x)==list else x
x=E()
while (y:=R(x,{}))!=x:x=y
print(F(x,0))


# def fmt(x, p):
#   z = type(x)
#   if z == tuple:
#     return f"(λ{x[0]}. {fmt(x[1],0)})"
#   elif z == list:
#     o=fmt(x[0],0)+" "+fmt(x[1],1)
#     return [o,f"({o})"][p]
#   else:
#     return x

# def reduce(x, env):
#   z = type(x)
#   if z == list:
#     return reduce(x[0][1], env|{x[0][0]:x[1]})
#   return env.get(x,x)

# def E():
#  if t[0]=="λ":return[[z(0),z(0),z(0)][1],E()]
#  x=A()
#  while t and t[0]!=")":x=(x,A())
#  return x

# def subst(exp, it, var):
#   z = type(exp)
#   if z == list:
#     return [subst(exp[1], it, var), exp[1]][exp == var]
#   elif z == tuple:
#     return (subst(exp[0], it, var), subst(exp[1], it, var))
#   else:
#     return {var: it}.get(exp, exp)

# def reduce(x):
#   z = type(x)
#   if z == tuple:
#     f=x[0]
#     a=x[1]
#     return subst(f[1], a, f[0])
#   else:
#     return x

# Q=lambda l,t,s:lambda*x:eval(g()[str(type(x[0]))[8]],g())

# F=Q('f"(λ{x[0][0]}. {F(x[0][1],0)})"'
