for n in range(1, 100):
    s = bin(n)[2:]
    if n % 2 == 0: s = s + "0"
    else: s = s + "1"
    if s.count("1") % 4 == 0: s = "11" + s[2:]
    if len(s) % 3 != 0: s = s[:-2] + "10"
    r = int(s, 2)
    if r <= 98: print(n)
