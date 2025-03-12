ans = []
xs = [int(x) for x in open('17.txt')]
def ch(x): return 10000 <= x < 10 ** 5 and x % 100 == 61
mx33 = max(x for x in xs if 100 <= x <= 1000 and x % 100 == 33)

for x, y, z in zip(xs, xs[1:], xs[2:]):
    if (ch(x) or ch(y) or ch(z)) and (x + y + z) >= mx33:
        ans.append(x + y + z)
print(len(ans), max(ans))
