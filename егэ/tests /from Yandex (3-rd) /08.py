from itertools import *
k = 0

for p in permutations("АРТЕМ"):
  s = "".join(p)
  if s[0] != "А" and s[0] != "Е" and s[-1] != "А" and s[-1] != "Е":
    k += 1
print(k)
