def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, a): return (nD(x, a) and 132 <= x <= 150) <= nD(x, 13)

for a in range(1, 100):
  if all(f(x, a) for x in range(1, 1000)): 
    print(a)
