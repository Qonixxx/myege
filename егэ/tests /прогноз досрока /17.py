ans = []
xs = [int(x) for x in open("17.txt")]
kr17 = min(x for x in xs if 1000 <= abs(x) <= 9999 and abs(x) % 17 == 0) ** 2
def ch(x): return 1000 <= abs(x) <= 9999 and abs(x) % 100 == 27
for x, y, z in zip(xs, xs[1:], xs[2:]):
    if (ch(x) or ch(y) or ch(z)) and (x ** 2 + y ** 2 + z ** 2) <= kr17:
        ans.append(abs(x) + abs(y) + abs(z))
print(len(ans), min(ans))
