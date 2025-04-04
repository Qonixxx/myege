def toBase(x):
    s = ""
    while x:
        s += str(x % 7)
        x //= 7
    return s
 
ans = []
for n in range(1, 1000):
    s = toBase(n)
    if s.count("3") % 2 == 0: 
      s = "3" + s + s[0]
    else: 
      s = "6" + s + s[-1]
    r = int(s, 7)
    if r < 16777:
        ans.append(r)
print(max(ans))
        
