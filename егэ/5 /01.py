# from: https://kompege.ru/variant?kim=25062004

for n in range(1, 1000):
    s = ""
    sm = 0
    while n:
        s += str(n % 3)
        sm += n % 3
        n //= 3
    if sm % 2 == 0:
        s + "1" + s + "2"
    else:
        s = "2" + s + "0"
    r = int(s, 3)
    if r > 100:
        print(r)
        break
      # ans = 165
