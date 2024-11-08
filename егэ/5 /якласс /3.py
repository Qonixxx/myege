for n in range(1, 100):
    s = bin(n)[2:]
    if s.count("1") > s.count("0"): s += "1"
    else: s += "0"
    r = int(s, 2)
    if r > 42: print(r)
