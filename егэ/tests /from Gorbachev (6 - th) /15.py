from itertools import combinations

def f(x):
    P = 3 <= x <= 83
    Q = 62 <= x <= 131
    A = a1 <= x <= a2
    return (not Q) <= ((not A) and P <= Q)

ox = [i / 4  for i in range(3 * 4, 131 * 4 + 1)]

m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        m.append(a2 - a1)
print(min(m))
