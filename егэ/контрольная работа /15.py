from itertools import *

def f(x):
  B = 30 <= x <= 41
  C = 50 <= x <= 56
  A = a1 <= x <= a2
  return (not((B or C) <= A))

ox = [i/4 for i in range(24 * 4, 76 * 4 + 1)]
m = []

for a1, a2 in combinations(ox, 2):
  if all(f(x) == 0 for x in ox):
    m.append(a2 - a1)
print(min(m)) # 26
