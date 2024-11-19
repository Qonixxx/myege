from itertools import *
k = 0

for x in product("012345678", repeat = 5):
    s = "".join(x)
    sc = s
    sc = sc.replace("3", "1").replace("5", "1").replace("7", "1")
    if s.count("0") == 1 and s[0] != "0" and "10" not in sc and "01" not in sc:
        k += 1
print(k)
# ans - 5120
