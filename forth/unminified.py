import re, sys

i = """

square { dup * }

main { 5 square print }

"""
tokens = re.findall("{|}|[^\s{}]+", i)

env = {
    "print": lambda: print(stack.pop()),
    "dup": lambda: (lambda x: stack.extend((x, x)))(stack.pop()),
    "*": lambda: stack.append(stack.pop() * stack.pop()),
}

def parse():
    t = tokens.pop(0)
    if t == "{":
        x = []
        while tokens[0] != "}":
            x.append(parse())
        tokens.pop(0)
        return x
    if t.isdigit():
        return int(t)
    else:
        return t

stack = []

def evaluate(expr):
    if type(expr) in (list, int):
        stack.append(expr)
    else:
        f = env[expr]
        if type(f) is list:
            for x in f:
                evaluate(x)
        else:
            f()

while tokens:
    n = tokens.pop(0)
    env[n] = parse()

evaluate("main")


