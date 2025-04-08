s = open("24.txt").readline()
l = mx = countAB = 0

for r in range(1, len(s)):
    if s[r] + s[r - 1] == "BA": countAB += 1
    while countAB > 100:
        if s[l] + s[l + 1] == "AB": countAB -= 1
        l += 1
    if countAB == 100: mx = max(mx, r - l + 1)
print(mx)
