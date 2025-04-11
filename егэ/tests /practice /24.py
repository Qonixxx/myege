s = open("24.txt").readline()
s = s.replace("F", "B").replace("D", "B").replace("C", "B").replace("E", "A")
l = m = cab = 0

for r in range(1, len(s)):
  if s[r - 1] + s[r] == "AB": cab += 1
  while cab > 130:
    if s[l] + s[l + 1] == "AB": cab -= 1
    l += 1
  if cab <= 130: m = max(m, r - l + 1)
print(m)
