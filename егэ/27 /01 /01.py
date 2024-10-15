with open("27_A_17834.txt") as f:
    k1 = []
    k2 = []
    for s in f:
        x, y = [float(c) for c in s.split()]
        if -3 <= x <= 6.5 and -4 <= y <= 6:
            k1.append([x, y])
        if 6 <= x <= 14 and 2 <= y <= 12:
            k2.append([x, y])

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
    print((x1 + x2) * 100 / 2, (y1 + y2) * 100 / 2)
