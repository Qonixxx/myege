xs = [int(x) for x in open("17.txt")]
ans = []
for x, y in zip(xs, xs[1:]):
    if str(x)[-1] == str(y)[-1] and x * y % 2 == 0:
        ans.append(x ** 2 + y ** 2)
print(len(ans), max(ans))
