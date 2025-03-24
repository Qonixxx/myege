with open("26.txt") as f:
  s, n = map(int, f.readline().split())
  xs = sorted([int(x) for x in f])

files = []
while sum(files) + xs[0] <= s:
  files += [xs[0]]
  xs.remove(xs[0])
print(len(files)) # ans1

for i in range(0, len(xs)):
  if sum(files) - files[-1] + xs[0] <= s:
    files[-1] = xs[0]
    xs.remove(xs[0])
print(files[-1]) # ans2
