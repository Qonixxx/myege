s = open("24.txt").readline()
m = 0 # длина самой большой подчепочки

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if "D" not in c:
            m = max(m, len(c))
        else: break
print(m)
