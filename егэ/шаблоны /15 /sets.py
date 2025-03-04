# множества

a = set()

def f(x):
    A = x in a
    B = x in {3, 6, 9, 12}
    C = x in {1, 2, 3, 4, 5, 6}
    return (not((not A) and B)) or (not(C))

# при минимальном множестве A
for x in range(1000):
    if f(x) == 0:
        a.add(x)
print(len(a))

'-----------------------------------------------------------------------------------------------------'
# при максимальном
a = set(range(1000))
p = set(range(2, 22, 2))
q = set(range(5, 55, 5))

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return (A <= P) and (Q <= (not A))


for x in range(1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))
