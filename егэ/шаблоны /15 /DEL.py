def f(x, a): return ((x % 84 != 0) or (x % 90 != 0)) <= (x % a != 0)

for a in range(1, 100000):
    if all(f(x, a) == 1 for x in range(1, 10000000)): print(a)
