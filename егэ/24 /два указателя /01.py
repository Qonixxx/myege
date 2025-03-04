'''
Определите максимальное количество идущих подряд символов, среди которых буквы X и Y встречаются ровно по одному разу, а буква A не встречается совсем.
'''
s = open("24.txt").readline()

l = kx = ky = 0
m = 0

for r in range(len(s)):
    if s[r] == "A":
        l = r + 1
        kx = ky = 0
    if s[r] == "X": kx += 1
    if s[r] == "Y": ky += 1
    while kx > 1 or ky > 1:
        if s[l] == "X": kx -= 1
        if s[l] == "Y": ky -= 1
        l += 1
    if kx == 1 and ky == 1:
        m = max(m, r - l + 1)
print(m)
