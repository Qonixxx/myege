def div(x): return sorted({i for d in range(2, int(x ** 0.5) + 1) if x % d == 0 for i in {d, x // d}})
def prime(x): return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
k = 0
for x in range(550001, 600000):
    if k == 6: break
    xs = div(x)
    if not xs: continue
    if not prime(max(xs)):
        print(x, max(xs))
        k += 1
    
'''
550002 275001
550004 275002
550005 183335
550008 275004
550010 275005
550011 183337
'''
