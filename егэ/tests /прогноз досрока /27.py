a = []

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]
    
def getCluster(p0):
    kl = [p for p in a if dist(p0, p) < 0.3]
    if len(kl) > 0:
        for p in kl: a.remove(p)
        nkl = [getCluster(p) for p in kl]
        for c in nkl: kl.extend(c)
    return kl
    
for s in open("27B.txt"): a.append([float(c) for c in s.split()])
print(len(a))

kls = []
while len(a) > 0:
    p0 = a.pop()
    kl = [p0] + getCluster(p0)
    print(len(kl))
    kls.append(kl)
print(len(kls))

centroids = [center(kl) for kl in kls]

px = sum(x for x, y in centroids) / len(kls)
py = sum(y for x, y in centroids) / len(kls)
print(int(px * 10 ** 4), int(py * 10 ** 4))
