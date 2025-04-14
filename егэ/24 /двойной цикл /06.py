s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if all(c[i] + c[i + 1] + c[i + 2] != c[i + 3] + c[i + 4]  + c[i + 5] for i in range(len(c) - 5)):
            m = max(m, len(c))
        else: break
print(m)
