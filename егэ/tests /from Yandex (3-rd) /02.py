from itertools import *

def f(a, b, c, d): return c and (a or d) and (d <= b)

for a in product([0, 1], repeat = 6):
  table = [(a[0], a[1], a[2], 0), (a[3], 1, 0, a[4]), (0, a[5], 1, 0)]
  if len(table) == len(set(table)):
    for p in permutations("abcd"):
      if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]: print(p)
