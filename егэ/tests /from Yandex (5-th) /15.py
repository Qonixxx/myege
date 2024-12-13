def D(x, d): return x % d == 0
def nD(x, d): return x % d != 0
def f(x, a): return (nD(x, 100) and D(x, 4)) or D(x, 400) or nD(x, a)

for a in range(1, 101):
  if all(f(x, a) for x in range(1, 1000)): print(a)
# ans - 16
