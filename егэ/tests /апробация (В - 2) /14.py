mx = -float('inf')
for x in range(2031):
    s = 3 ** 100 - x
    xs = []
    while s:
        xs += [s % 3]
        s //= 3
    if xs.count(0) == 1 and x > mx: mx = x
print(mx)
