with open("26.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    xs = []
    for i in range(n):
        st, end = map(int, f.readline().split())
        xs.append([st, end])
xs.sort()

camera = [0] * (k + 1)
last = cnt = 0
for i in range(len(xs)):
    st, end = xs[i]
    for j in range(1, k):
        if xs[j] < st:
            xs[j] = end
            cnt += 1
            last = j
print(cnt, last)
