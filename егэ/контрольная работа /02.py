from itertools import *

def f(x, y, w, z): return (x and y) or (y == z) or w

for a in product([0, 1], repeat = 4):
    table = [(1, a[0], 0, 0), (a[1], 1, a[2], 0), (1, 0, 1, a[3])]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
                print(p)
