# with open("test.txt") as f:
with open("26.txt") as f:
    k, m, l = [int(x) for x in f.readline().split()]
    n = int(f.readline())
    data = sorted([[int(x) for x in f.readline().split()] for _ in range(n)])
    storage = [[[-1] * l for _ in range(m)] for z in range(k)]
    stat = [[0] * m for _ in range(k)]
    for st, end in data:
        status = 1 
        for stel in range(k):
            for row in range(m):
                for place in range(l):
                    if status and storage[stel][row][place] < st:
                        storage[stel][row][place] = end
                        stat[stel][row] += 1
                        status = 0
print(sum([sum(row) for row in stat]), stat[0].index(min(stat[0])) + 1)
