from itertools import *
cnt = 0
num = 1
for a in product(sorted("ВЕЧНОСТЬ"), repeat = 6):
  s = "".join(a)
  if (s[0] not in "ВЧНСТЬ" and s.count("О") >= 2) \
      and (num % 2 == 0):
    cnt += 1
  num += 1
print(cnt)
