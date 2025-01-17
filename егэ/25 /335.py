def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
k = 0
for x in range(800000, 10 ** 6):
    if k == 9: break
    xs = div(x)
    for i in xs:
        if i % 10 == 9 and i != 9:
            print(x, i)
            break
    k += 1
