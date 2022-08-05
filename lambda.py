#i=__import__
#t=i('re').findall(r'[().λ]|[a-z]+',i("sys").stdin.read()')

i = "(λx. x)(λx. x)"
t=__import__('re').findall(r'[().λ]|[a-z]+',i)
z=t.pop

# def E():
#  if t[0]=="λ":return[[z(0),z(0),z(0)][1],E()]
#  x=A()
#  while t and t[0]!=")":x=(x,A())
#  return x

E=lambda:[[z(0),z(0),z(0)][1],E()]if t[0]=="λ"else(lambda x:x if t and t[0]==")"else(x,A()))(A())

A=lambda:(m:=z(0))and([E(),z(0)][0]if m=="("else m)


def fmt(x, p):
  z = type(x)
  if z == list:
    return f"(λ{x[0]}. {fmt(x[1],0)})"
  elif z == tuple:
    o=fmt(x[0],0)+" "+fmt(x[1],1)
    return [o,f"({o})"][p]
  else:
    return x

def subst(exp, it, var):
  z = type(exp)
  if z == list:
    return [subst(exp[1], it, var), exp[1]][exp == var]
  elif z == tuple:
    return (subst(exp[0], it, var), subst(exp[1], it, var))
  else:
    return {var: it}.get(exp, exp)

def reduce(x):
  z = type(x)
  if z == tuple:
    f=x[0]
    a=x[1]
    return subst(f[1], a, f[0])
  else:
    return x

x=E()
while (y:=reduce(x))!=x:x=y

print(fmt(x,0))
