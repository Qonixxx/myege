s = open("24.txt").readline()

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = [l:r + 1]
        if all(c[i] != c[i + 1] for i in range(len(c) - 1)):
            m = max(m, len(c))
        else: break
print(m)
