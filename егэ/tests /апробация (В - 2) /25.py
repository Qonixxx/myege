def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})

k = 0
M = 0
for x in range(7 * 10 ** 5, 8 * 10 ** 5):
    if k == 5: break
    xs = div(x)
    if len(xs) < 2:
        continue
    else:
        M = max(xs) + min(xs)
        if M % 10 == 4:
            print(x, M)
            k += 1

'''
700004 350004
700009 41194
700023 233344
700024 350014
700044 350024
'''
