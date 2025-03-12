from itertools import *

def f(x, y, w, z): return (((x or (not y)) <= (not(y <= z))) and w) # пишем собственное выражение, данное в условии  

for a in product([0, 1], repeat = (6)):
    table = [(1, a[0], 0, a[1]), (1, 1, a[2], 0), (a[3], a[4], 1, a[5])]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
