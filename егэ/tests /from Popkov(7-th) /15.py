def f(x, a): return (x & 45 != 0) <= ((x & 32 == 0) <= (x & a != 0))

for a in range(1, 1000):
    if all(f(x, a) == 1 for x in range(1, 500)):
        print(a)
        break
