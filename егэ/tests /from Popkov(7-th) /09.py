from itertools import combinations
k = 0

def ch(xs):
    xs = sorted(xs)
    return xs[2] / xs[1] == xs[1] / xs[0] and xs[1] / xs[0] != 1

for s in open("09.txt"):
    xs = [int(x) for x in s.split()]
    if any(ch(x) for x in combinations(xs, 3)): k += 1
print(k)
