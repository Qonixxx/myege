from itertools import combinations

def f(x):
    P = 17 <= x <= 61
    Q = 39 <= x <= 91
    A = a1 <= x <= a2
    return (Q and not A) and (A or not P)

ox = [i / 4 for i in range(17 * 4, 92 * 4)]

m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 0 for x in ox):
        m.append(a2 - a1)
print(min(m)) # 29.75 -> 30
