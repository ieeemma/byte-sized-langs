i=__import__
t=i('re').findall(r'[().λ]|[a-z]+',i("sys").stdin.read())
z=t.pop
T=type
class Q(tuple):...
E=lambda:([z(0),z(0),z(0)][1],E())if t[0]=="λ"else(lambda x:x if t and t[0]==")"else Q([x,A()]))(A())
A=lambda:(m:=z(0))and([E(),z(0)][0]if m=="("else m)
F=lambda x,p:f"(λ{x[0]}. {F(x[1],0)})"if T(x)==tuple else((o:=F(x[0],0)+" "+F(x[1],1))and[o,f"({o})"][p])if T(x)==Q else x
R=lambda x,e:(f:=R(x[0],e))and R(f[1],e|{f[0]:R(x[1],e)})if T(x)==Q else e.get(x,x)
x=E()
while (y:=R(x,{}))!=x:x=y
print(F(x,0))



# N = 0

# def R(x,e):
#   global N
#   # if N==500:exit()
#   print(" "*2*N + "eval " + F(x,0) + " under " + repr({k:F(v,1) for k,v in e.items()}))
#   N+=1
#   if T(x)==Q:
#     f=R(x[0],e)
#     # print(F(x[0],0), F(f,0), e)
#     o=R(f[1], e|{f[0]:R(x[1],e)})
#   else:o=e.get(x,x)

#   N-=1
#   print(" "*2*N + "=> " + F(o,0))
#   return o

# print(F(rx, 0))





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
