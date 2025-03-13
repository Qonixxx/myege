k = 1
for s in open("09.txt"):
    xs = [int(x) for x in s.split()]
    a2 = [x for x in xs if xs.count(x) == 2]
    a1 = [x for x in xs if xs.count(x) == 1]
    ev = [x for x in xs if x % 2 == 0]
    odd = [x for x in xs if x % 2 != 0]
    if (len(a2) == 6 and len(a1) == 1) and (sum(ev) < sum(odd)):
        print(k)
        break
    k += 1
