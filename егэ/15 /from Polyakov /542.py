def f(x, y): return (x < a) or (y < a) or ((x + 2 * y) > 50)

for a in range(1, 100):
    if all(f(x, y) == 1 for x in range(1, 300) for y in range(1, 300)):
        print(a) # ans = 17
        
        
