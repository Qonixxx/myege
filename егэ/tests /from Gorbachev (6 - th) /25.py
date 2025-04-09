from fnmatch import *
k = 0
for x in range(0, 10 ** 7, 25):
  if fnmatch(str(x), '89?45*75'):
    print(x, x // 25)
