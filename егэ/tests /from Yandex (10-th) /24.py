s = open("24.txt").readline()
l = m = cnt = 0
s = s.replace("E", "A")
s = s.replace("F", "B").replace("D", "B").replace("C", "B")

for r in range(1, len(s)):
  if s[r] == "B" and s[r - 1] == "A": cnt += 1
  while cnt > 130:
    if s[l] + s[l + 1] == "AB":
      cnt -= 1
    l += 1
  m = max(m, r - l + 1)
print(m)
