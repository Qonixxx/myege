with open("27A.txt") as f:
# with open("27B.txt") as f:
    f.readline()
    data = []
    for s in f:
        s = s.replace(",", ".")
        p = [float(c) for c in s.split()]
        data.append(p)
        
    def dist(p1, p2):
        x1, y1, x2, y2 = *p1, *p2
        return max(abs(x2 - x1), abs(y2 - y1))
        
    def getCluster(p0):
        cluster = [p for p in data if dist(p0, p) < 0.6]
        if len(cluster) > 0:
            for p in cluster: data.remove(p)
            nextkl = [getCluster(p) for p in cluster]
            cluster += sum(nextkl, [])
        return cluster
        
    clusters = []
    while len(data) > 0:
        p0 = data.pop()
        cluster = [p0] + getCluster(p0)
        clusters.append(cluster)
        
    k = len(clusters)
    
    def center(kl):
        m = []
        for p in kl:
            s = sum(dist(p, p1) for p1 in kl)
            m.append([s, p])
        return min(m)[1]
        
    centroid = [center(kl) for kl in clusters]
    
    px = sum(x for x, y in centroid)
    py = sum(y for x, y in centroid)
    print(int(px / k * 10 ** 4), int(py / k * 10 ** 4))
