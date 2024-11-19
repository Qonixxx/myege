from itertools import *
k = 0

for x in product("012345", repeat = 6):
    s = "".join(x)
    if s[0] != "0" and s[0] != "2" and "22" not in s and "33" not in s:
        k += 1
print(k)
# ans - 24283
