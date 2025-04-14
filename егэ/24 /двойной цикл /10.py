s = open("24.txt").readline()
s = s.replace("B", "A").replace("C", "A").replace("3", "1").replace("2", "1")
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if len(c) % 3 == 0:
            if all(c[i] + c[i + 1] + c[i + 2] == "1A1" for i in range(0, len(c), 3)):
                m = max(m, len(c))
            else: break
print(m // 3)
