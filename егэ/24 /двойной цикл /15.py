s = open("24.txt").readline()
m = float("inf")

for l in range(len(s)):
    for r in range(l, l + m):
        c = s[l:r+1]
        if c.count(".") == 7:
            m = min(m ,len(c))
            break
print(m)
