from sys import *
setrecursionlimit(10000)
def f(n): return n if n > 3000 else f(n + 2) + 2
print(f(40) - f(44))
