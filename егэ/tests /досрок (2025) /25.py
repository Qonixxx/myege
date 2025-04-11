def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
k = 0
for x in range(1125000, 1200000):
    if k == 5: break
    d = [i for i in div(x) if i % 10 == 7 and i != 7]
    if len(d) > 0: 
        print(x, d[0])
        k += 1
