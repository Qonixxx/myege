from itertools import *
k = 0

for x in permutations("ОЛИВИЯ"):
    s = "".join(x)
    if s[0] == "О" or s[0] == "Я" and "ЛИВИ" not in s:
        k += 1
print(k)
# ans - 236
