# 27A
with open("27A.txt") as f:
    k1 = []
    k2 = []
    for s in f:
        x, y = [float(c) for c in s.split()]
        if -2 <= x <=1 and 0 <= y <= 3:
            k1.append([x, y])
        if 1 <= x <= 4.5 and 3 <= y <= 7:
            k2.append([x, y])

    def get_center(k):
        mn = 10 ** 20
        xc = yc = 0
        for i in range(len(k)):
            x1, y1 = k[i]
            s = 0
            for j in range(len(k)):
                x2, y2 = k[j]
                s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            if s < mn:
                mn, xc, yc = s, x1, y1
        return xc, yc

    x1, y1 = get_center(k1)
    x2, y2 = get_center(k2)
    print((x1 + x2) * 10000 / 2, (y1 + y2) * 10000 / 2)

#27B
F = open("27B.txt")
k1 = []
k2 = []
k3 = []
for s in F:
    x, y = [float(c) for c in s.split()]
    if 0 <= x <= 3 and 0 <= y <= 4:
        k1.append([x, y])
    if 2 <= x <= 5 and 6 <= y <= 12:
        k2.append([x, y])
    if 5 <= x <= 8 and 2 <= y <= 8:
        k3.append([x, y])

def getCenter(xs):
    mn = 10 ** 20
    xc = yc = 0
    for i in range(len(xs)):
        x1, y1 = xs[i]
        s = 0
        for j in range(len(xs)):
            x2, y2 = xs[j]
            s += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if s < mn:
            mn, xc, yc = s, x1, y1
    return xc, yc


x1, y1 = getCenter(k1)
x2, y2 = getCenter(k2)
x3, y3 = getCenter(k3)
print((x1 + x2 + x3) * 10000 / 3, (y1 + y2 + y3) * 10000 / 3)

