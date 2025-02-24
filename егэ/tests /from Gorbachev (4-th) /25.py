from fnmatch import *
k = 0
for x in range(0, 10 ** 8, 111):
  if fnmatch(str(x), '3*4?5*6?') and x % 2 == 0:
    k += 1
print(k)
