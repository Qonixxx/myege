for n in range(1, 100):
    s = bin(n)[2:]
    for i in range(2): s += str(s.count("1") % 2)
    r = int(s, 2)
    if r < 65: print(r)
