b = [i for i in range(70, 91)]
for a in range(1, 100):
    f = 0
    for x in range(1, 301):
        if ((x % a == 0) or ((x in b) <= (x % 22 != 0))) == False:
            f = 1
            break
    if (f == 0):
        print(a)
# ans = 88
