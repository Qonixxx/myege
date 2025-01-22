# ЕГЭКР
data = []

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
def getCluster(p0):
    kl = [p for p in data if dist(p0, p) < 2]
    if len(kl) > 0:
        for p in kl: data.remove(p)
        nextkl = [getCluster(p) for p in kl]
        for c in nextkl: kl.extend(c)
    return kl
    
def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]
    
for s in open("27B.txt"):
    s = s.replace(",", ".")
    p = [float(c) for c in s.split()]
    data.append(p)
print("all dots:", len(data))

clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    print("dots in cluster:", len(cluster))
    clusters.append(cluster)
print("count of clusters:", len(clusters))

centroid = [center(kl) for kl in clusters]

px = sum(x for x, y in centroid) / len(clusters)
py = sum(y for x, y in centroid) / len(clusters)
print(abs(int(px * 10000)), abs(int(py * 10000)))
