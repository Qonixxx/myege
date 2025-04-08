k = 0
for s in open('09.txt'):
    xs = [int(x) for x in s.split()]
    ch1 = [x for x in xs if xs.count(x) == 2]
    if len(ch1) == 2 and max(xs) < sum(xs) - max(xs): k += 1
print(k)
