#i=__import__
#t=i('re').findall(r'[().λ]|[a-z]+',i("sys").stdin.read()')

i = "(λx. x)(λx. x)"
t=__import__('re').findall(r'[().λ]|[a-z]+',i)

def expr():
  if t[0] == "λ":
    t.pop(0)
    n = t.pop(0)
    t.pop(0)
    return [n, expr()]
  else:
    return app()

def app():
  x = atom()
  while t and t[0] != ")":
    x = (x, atom())
  return x

def atom():
  s = t.pop(0)
  if s == "(":
    x = expr()
    t.pop(0)
    return x
  else:
    return s

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

x=expr()
while (y:=reduce(x))!=x:x=y

print(fmt(x,0))
