with open("27A.txt") as f:
# with open("27B.txt") as f:
    f.readline() # читаем первую строку "в пустоту"
    data = [] 
    for s in f:
        s = s.replace(",", ".") # если файл "кривой"
        p = [float(c) for c in s.split()] 
        data.append(p)
    
    # ф-ла в условии     
    def dist(p1, p2):
        x1, y1, x2, y2 = *p1, *p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # автоматическое разделение на кластеры
    def getCluster(p0):
        cluster = [p for p in data if dist(p0, p) < 1] # для 27А
        # cluster = [p for p in data if dist(p0, p) < 0.3] 
        if len(cluster) > 0:
            for p in cluster: data.remove(p) 
            next_cluster = [getCluster(p) for p in cluster] 
            cluster += sum(next_cluster, [])
        return cluster
    
    clusters = [] 
    while len(data) > 0: 
        p0 = data.pop() 
        cluster = [p0] + getCluster(p0) 
#       print(len(cluster))
        clusters.append(cluster)
        
    k = len(clusters) 
        
    def centr(kl):
        m = []
        for p in kl:
            s = sum(dist(p, p1) for p1 in kl) 
            m.append([s, p])
        return min(m)[1]
        
    centroid = [centr(kl) for kl in clusters] 
    
    px = sum(x for x, y in centroid)
    py = sum(y for x, y in centroid)
    print(int(px / k * 10000), int(py / k * 10000))
