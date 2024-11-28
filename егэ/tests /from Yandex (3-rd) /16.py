from sys import *

setrecursionlimit(10000)

def f(n): 
  if n == 41: return 41
  if n > 41 and n % 2 == 0: return f(n - 1) - n
  else: return n * f(n - 2)
print(f(9094) / f(9089))
