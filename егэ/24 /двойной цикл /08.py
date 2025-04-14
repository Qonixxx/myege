s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = [l:r + 1]
        if len(c) % 2 == 0:
            if all(c[i] + c[i + 1] in ["AA", "CC"] for i in range(0, len(c), 2)):
                m = max(m, len(c))
            else: break
print(m // 2)
