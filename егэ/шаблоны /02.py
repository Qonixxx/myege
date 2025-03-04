from itertools import *

def f(x, y, w, z): return () # пишем собственное выражение, данное в условии  

for a in product([0, 1], repeat = ()):
    table = [(), (), ()]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in table] == []:
                print(p)
