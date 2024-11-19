from itertools import *
k = 0

for x in product("0123456789", repeat = 6):
    s = "".join(x)
    if s.count("1") >= 2 and s[0] != "0" and s[-1] != "2" and s[-1] != "3" \
       and int(s[0]) % 2 == 0:
        k += 1
print(k)
# ans - 28400
