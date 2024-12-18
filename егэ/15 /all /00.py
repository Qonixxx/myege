from itertools import *

def f(x):
  # пишем границы отрезков из условия в формате P = 25 <= x <= 50
  A = a1 <= x <= a2
  # переписываем выражение из условия в return, указывая заданные отрезки (P, A и т.д)

ox = [i/4 for i in range(24 * 4, 76 * 4 + 1)]
m = []

for a1, a2 in combinations(ox, 2):
  if all(f(x) == 1 for x in ox):
    m.append(a2 - a1)
print(min(m))
