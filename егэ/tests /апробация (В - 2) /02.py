from itertools import *

def f(x, y, z, w): return (not(x <= y) or (z <= w) or (not z))

for a in product([0, 1], repeat = 7):
    table = [(a[0], 0, a[1], 0), (1, a[2], a[3], a[4]), (0, 1, a[5], a[6])]
    if len(table) == len(set(table)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
