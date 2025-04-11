xs = [int(x) for x in open("17.txt")]
mx = max(x for x in xs if 10 <= x <= 99)
ans = [x + y for x, y in zip(xs, xs[1:]) if ((10 <= abs(x) <= 99) or (10 <= abs(y) <= 99)) and x + y <= mx]
print(len(ans), max(ans))
