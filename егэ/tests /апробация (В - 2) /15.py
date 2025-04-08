from itertools import combinations

def f(x):
    P = 17 <= x <= 58
    Q = 29 <= x <= 80
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

ox = [i / 4  for i in range(17 * 4, 80 * 4 + 1)]

m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        m.append(a2 - a1)
print(min(m))
# 29
