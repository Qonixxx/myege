from itertools import *

k = 1
for a in product("АКОРХ", repeat = 6):
    s = "".join(a)
    if s[0] == "О" and "АА" not in s:
        print(k, s)
        break
    k += 1
# ans - 6381
