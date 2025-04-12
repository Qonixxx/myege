from itertools import *
cnt = 0
for x in product("0123456789AB", repeat = 5):
  s = "".join(x)
  if s[0] != "0" and s.count("7") == 1 and len([x for x in s if x in "9AB"]) <= 3:
    cnt += 1
print(cnt)
