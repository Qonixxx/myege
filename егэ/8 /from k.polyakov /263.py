from itertools import *
k = 0

for x in product("012345678", repeat = 5):
    s = "".join(x)
    if int(s[0]) % 2 == 0 and s[0] != "0" and (s[-1] != "1" or s[-1] != "8") and s.count("3") <= 1:
        k += 1
print(k)
# ans - 24576
