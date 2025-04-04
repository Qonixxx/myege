k = 0
for s in open("9.txt"):
    xs = [int(x) for x in s.split()]
    ch1 = [x for x in xs if xs.count(x) == 3]
    ch3 = [x for x in xs if x == min(xs) and xs.count(x) > 1]
    ch2 = [x for x in xs if xs.count(x) == 1]
    if len(ch1) + len(ch2) == len(xs) or (len(ch3) + len(ch2) == len(xs)):
        k += 1
print(k)
