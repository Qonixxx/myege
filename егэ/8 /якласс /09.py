from itertools import *
k = 0

for x in product("012345678", repeat = 5):
    s = "".join(x)
    if s[0] != "0" and s[0] != "4" and (int(s[0]) + int(s[2]) == int(s[3])) and ((int(s[1]) + int(s[4])) % 2 == 0):
        k += 1
print(k)
# ans - 1271
