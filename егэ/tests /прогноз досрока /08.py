from itertools import *

k = 1
for x in product(sorted("МАКС"), repeat = 6):
    s = "".join(x)
    if "КК" not in s and s.count("С") == s.count("М") == 0:
        print(k, s)
    k += 1
    
