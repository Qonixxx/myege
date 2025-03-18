def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
for x in range(226849, 226871 + 1):
    if len(div(x)) == 2: print(1, *div(x), x)
