from itertools import *

def f(x, y, z): return (x == y) or ((y or z) <= x)

for a in product([0, 1], repeat = 3):
    table = [(a[0], 1, 1), (a[1], a[2], 1)]
    if len(table) == len(set(table)):
        for p in permutations("xyz"):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0]:
                print(p)
