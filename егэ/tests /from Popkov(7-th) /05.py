def base(x):
    s = ''
    while x:
        s += str(x % 3)
        x //= 3
    return s

for n in range(1, 300):
    s = base(n)
    if sum(map(int, s)) % 2 == 0:
        s = "12" + s[2:] + "0"
    else:
        s = "10" + s[2:] + "2"
    r = int(s, 3)
    if r > 105:
        print(r)
        break
