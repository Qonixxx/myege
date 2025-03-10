ans = 0
for x in range(1, 1001):
    s = 5 ** x + 31 ** 31 - 46 ** 17 - x
    xs = []
    while s:
        xs += [s % 7]
        s //= 7
    if 100 < xs.count(6) < 1000:
        ans += 1
print(ans)
