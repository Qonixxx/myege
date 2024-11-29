#https://github.com/sw793/ege/tree/main/Sorted/15/DEL
from itertools import combinations

def f(x):
    P = 25 <= x <= 50
    Q = 30 <= x <= 90
    A = a1 <= x <= a2
    return ((not A) <= (not P)) <= (A <= Q)
    
ox = [i / 4 for i in range(25 * 4, 91 * 4)]

    
m = []
for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        m.append(a2 - a1)
print(max(m)) # 60
