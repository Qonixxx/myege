for n in range(1, 35):
    s = bin(n)[2:]
    if n % 3 == 0: s = "101" + s[3:]
    else: s = s[:-3] + "111"
    r = int(s, 2)
    if r > 30:
        print(r)
