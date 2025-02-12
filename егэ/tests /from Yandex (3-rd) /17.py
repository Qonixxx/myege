xs = [int(x) for x in open("17.txt")]
ans = []

def ch(x): return (1000 <= abs(x) <= 10000) and (abs(x) % 100 == 42)
mx42 = max(x for x in xs if ch(x))

for x, y, z in zip(xs, xs[1:], xs[2:]):
  if ((x + y + z) > mx42) and ((ch(x) and ch(y)) or (ch(y) and ch(z)) or (ch(x) and ch(z))):
    ans.append(x + y + z)

print(len(ans), max(ans))
