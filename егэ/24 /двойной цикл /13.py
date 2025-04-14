s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if "V" not in c and "X" not in c and "Z" not in c:
            if all(c.count(x) <= 8 for x in "AEIOUY"):
                m = max(m, len(c))
            else: break
        else: break
print(m)
