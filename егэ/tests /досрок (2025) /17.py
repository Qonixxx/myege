ans = []
xs = [int(x) for x in open("17.txt")]
need = [x for x in xs if x < 0]

for x, y, z in zip(xs, xs[1:], xs[2:]):
    if max(x, y, z) * min(x, y, z) > sum(need): 
        ans.append((x + y + z))
print(len(ans), abs(max(ans)))
