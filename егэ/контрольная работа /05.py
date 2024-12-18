for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 2 == 0: s = s + "01"
    else: s = s + "10"
    r = int(s, 2)
    if r > 82:
        print(r)
        break
