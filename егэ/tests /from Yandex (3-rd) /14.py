mx = -100000000
for x in range(1, 1951):
  s = 72070 + 7400 - x
  a = []
  while s:
    a += [s % 9]
    s //= 9
  if a.count(0) > mx: mx = a.count(0)
print(mx)
