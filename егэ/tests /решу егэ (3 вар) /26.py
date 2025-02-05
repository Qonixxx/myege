with open("26.txt") as f:
    s, n = map(int, f.readline().split())
    xs = sorted([int(x) for x in f]) # сортируем список по восрастанию
    res = [] # все файлы, загруженные на диск
    
    for i in range(len(xs)):
        if xs[i] + sum(res) <= s: 
            res.append(xs[i])
            xs[i] = 0
        else:
            break

    for i in range(len(xs)):
        if xs[i] == 0: continue
        if (sum(res) - res[-1] + xs[i]) <= s:
            res.pop()
            res.append(xs[i])
            xs[i] = 0
print(len(res), max(res))
