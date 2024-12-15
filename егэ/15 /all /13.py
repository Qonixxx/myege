a = set()
p = set(range(2, 22, 2))
q = set(range(3, 33, 3))
r = set(range(12, 72, 12))

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    R = x in r
    return (not A) <= ((P and Q) <= R)

for x in range(1000):
    if f(x) == 0:
        a.add(x)

prod = 1

for q in a:
    prod *= q

print(prod)
