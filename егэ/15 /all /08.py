def f(x, y, a): return ((2 * x + y) != 70) or (x < y) or (a < x)

for a in range(1000, 0, -1):
    if all(f(x, y, a) == 1 for x in range(1, 500) for y in range(1, 500)):
        print(a)
        break # ans - 28
        
