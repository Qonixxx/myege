xs = [int(x) for x in open("17.txt")]
ans = [x + y for x, y in zip(xs, xs[1:]) if x % 16 == min(xs) or y % 16 == min(xs)]
print(len(ans), max(ans))
