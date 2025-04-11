def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
def prime(x): return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

k = 0
for x in range(550001, 600000):
    if k == 5: break
    d = [i for i in div(x) if prime(i)]
    if len(d) > 0:
        if sum(d) > 2000 and sum(d) % 10 == 7:
            print(x, sum(d))
            k += 1
    
