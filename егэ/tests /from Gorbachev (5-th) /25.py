def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
k = 0
for x in range(900000):
    if k == 7: break
    if len(div(x)) > 1:
        m = max(div(x)) + min(div(x))
    else: m = 0
    m = str(m)
    if m[0] == "7" and m[-1] == "7":
        print(x, int(m))
        k += 1
