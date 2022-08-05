#i=__import__
#t=i('re').findall(r'[().λ]|[a-z]+',i("sys").stdin.read()')


i="λz. (λy. y (λx. x)) (λx. z x y) "
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

# def α(exp, it, var):
#   z = type(exp)
#   if z == list:
#     return [α(exp[1], it, var), exp[1]][exp == var]
#   elif z == tuple:
#     return (α(exp[0], it, var), α(exp[1], it, var))
#   else:
#     return {it: var}.get(exp, exp)


print(fmt(expr(), 0))
