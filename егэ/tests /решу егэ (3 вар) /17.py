xs = [int(x) for x in open("17.txt")]
def ch(x, y): return (x + y) % 8 == 0
ans = []
for x, y in zip(xs, xs[1:]):
    if ch(x, y): ans.append(x + y)
print(len(ans), max(ans))
