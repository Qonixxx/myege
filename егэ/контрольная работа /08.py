from itertools import *
k = 1
for a in product(sorted("АБЗИ"), repeat = 4):
    s = "".join(a)
    if s == "ИЗБА":
        print(k)
        break
    k += 1
