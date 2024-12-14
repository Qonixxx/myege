# комп егэ (№1)
def f(x, a): return (x % a == 0 and x % 24 == 0 and x % 16 != 0) <= (x % a != 0)

for a in range(1, 101):
  if all(f(x, a) for x in range(1, 1000)): print(a) # ans - 16
