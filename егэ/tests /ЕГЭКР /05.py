def c3(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    return s

m = []
for n in range(1, 1000):
    b = c3(n)
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + c3(sum(map(int, b)))
    r = int(b, 3)
    if r % 2 == 0 and r > 220:
        print(r)
        break
