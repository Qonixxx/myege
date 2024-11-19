from itertools import *
k = 1
xs = []

for x in product(sorted("МАНГУСТ"), repeat = 6):
    s = "".join(x)
    if s[0] != "У" and s.count("М") == 2 and s.count("Г") <= 1:
       xs.append([k, s])
    k += 1
print(xs[-1])
#ans = 100810
