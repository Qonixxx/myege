for n in range(1, 1000):
    s = bin(n)[2:]
    for i in range(2): s += str(sum(map(int, s)) % 2)
    if int(s, 2) > 80:
        print(int(s, 2))
        break
