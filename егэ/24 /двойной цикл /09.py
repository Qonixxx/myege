s = open("24.txt").readline()
s = s.replace("B", "A").replace("C", "A").replace("2", "1").replace("3", "1")
m = 0

for l in range(len(c)):
    for r in range(l + m, len(c)):
        c = s[l:r + 1]
        if len(c) % 2 == 0:
            if all(c[i] + c[i + 1] == "A1" for i in range(0, len(c), 2)):
                m = max(m, len(c))
            else: break
print(m // 2)
