from sys import *
setrecursionlimit(10000)

def f(n): return n if n < 52 else 3 * f(n - 2)
print(f(15127) // f(15099))
