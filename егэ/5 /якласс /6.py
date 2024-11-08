k = 0
for n in range(1, 1000):
    s = bin(n)[2:]
    for i in range(2): s += str(s.count("1") % 2)
    r = int(s, 2)
    if r >= 200 and r <= 500:
        k += 1
print(k)
