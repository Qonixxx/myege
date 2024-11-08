for n in range(1, 300):
    s = bin(n)[2:]
    s1 = s + s[-1]
    if s.count("1") % 2 == 0: s1 += "0"
    else: s1 += "1"
    if s1.count("1") % 2 != 0: s1 += "1"
    else: s1 += "0"
    r = int(s1, 2)
    if r > 150: print(r)
