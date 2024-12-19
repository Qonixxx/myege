def t(x): return x % 10 != 3
def q(x): return x ** 2

xs = [int(x) for x in open("17.txt")]
ans = []
for i in range(len(xs) - 2):
    if (t(xs[i]) and t(xs[i + 1]) and t(xs[i + 2])) and ((q(xs[i]) + q(xs[i + 1]) + q(xs[i + 2])) > max(xs)):
        ans.append(q(xs[i]) + q(xs[i + 1]) + q(xs[i + 2]))
print(len(ans), min(ans))

