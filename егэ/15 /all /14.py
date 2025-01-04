# https://inf-ege.sdamgia.ru/problem?id=9653
from itertools import combinations 

def f(x):
    P = 10 <= x <= 29
    Q = 13 <= x <= 18
    A = a1 <= x <= a2
    return (A <= P) or Q
    
ox = [i / 4 for i in range(10 * 4, 30 * 4 + 1)]
m = []

for a1, a2 in combinations(ox, 2):
    if all(f(x) == 1 for x in ox):
        m.append(a2 - a1)
print(max(m))

# решение с решу егэ
p = [int(i) for i in range(10,30)]
q = [int(i) for i in range(13,19)]
a = [int(i) for i in range(10,30)]
for x in range(1,100):
    if not(((x in a) <= (x in p)) or (x in q)):
        a.remove(x)
print(len(a) - 1)
