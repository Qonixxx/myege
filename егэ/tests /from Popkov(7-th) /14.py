ans = 0
for x in range(1, 2006):
    s = 12 ** 1120 + 12 ** 100 - x
    xs = []
    while s:
        xs += [s % 12]
        s //= 12
    if xs.count(0) == 1022 and x > ans: ans = x
print(ans)
        
