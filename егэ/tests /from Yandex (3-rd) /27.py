# https://education.yandex.ru/ege/variants/5fc3c948-182b-495f-9d5a-acff30e93c71/task/27
from math import *

with open("27_B.txt") as f:
    data = []
    for s in f:
        p = [float(c) for c in s.split()]
        data.append(p)
    for i in range(len(data)):
        data[i][0] = cos(data[i][0])
        data[i][1] = sin(data[i][1])

    def dist(p1, p2):
        x1, y1, x2, y2 = *p1, *p2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    def getCluster(p0):
        cluster = [p for p in data if dist(p0, p) < 1] # список из точек, которые находятся в ближайшей окрестности от p0
        if len(cluster) > 0:
            for p in cluster: data.remove(p) # удаляем точки из общ.списка, чтобы повторно их не брать
            next_cluster = [getCluster(p) for p in cluster] # для тех точек, которых мы нашли, ищем соседей 
            cluster += sum(next_cluster, [])
        return cluster

    clusters = [] 
    while len(data) > 0: # пока точки в списке есть
        p0 = data.pop() 
        cluster = [p0] + getCluster(p0) # берем первую точку и находим для нее класиер
#       print(len(cluster))
        clusters.append(cluster)

    def centr(kl):
        m = []
        for p in kl:
            s = sum(dist(p, p1) for p1 in kl) # посчитали расстояние точки до каждой из точек кластора и сложили
            m.append([s, p])
        return min(m)[1]

    centroid = [centr(kl) for kl in clusters]    
    k = len(clusters)

    px = sum(x for x, y in centroid)
    py = sum(y for x, y in centroid)
    print(int(px / k * 10000), int(py / k * 10000))
