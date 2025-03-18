from sys import *
setrecursionlimit(10000)
def f(n): return n if n < 110 else n + f(n - 1)
print(f(2025) - f(2021))
