from itertools import *

def f(x, y, w, z): return ((not x) and y and z and (not w)) or \
    ((not x) and y and (not z) and w) or (x and y and z and (not w))
    
for a in product([0, 1], repeat = 7):
    table = [(1, a[0], a[1], a[2]), (0, a[3], 1, a[4]), (a[5], 0, 0, a[6])]
    if len(table) == len(set(table)):
        for p in permutations("xywz"):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(p)
