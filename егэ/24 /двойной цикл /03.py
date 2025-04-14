s = open("24.txt").readline()
for x in "QWERTYUIOPSDFGHJKLZXCVBNM": s = s.replace(x, "A")
for n in "023456789": s = s.replace(n, "1")

m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r+1]
        if "AA" not in s and "11" not in s:
            m = max(m, len(c))
        else: break
print(m)
