from itertools import product
k = 0
for p in product("ИМПЛАНТ", repeat = 5):
    if p.count("М") == 1: k += 1
print(k)
