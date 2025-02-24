s = open("24.txt").readline()
s = s.replace("+", "*")
for x in "123456789":
    s = s.replace(x, "9")
mx = 0
s = s.split("*")
res = []
for c in s:
    if c != "" and c[:2] != "00" and c[:2] != "09":
        res.append(c)
        mx = max(mx, len("*".join(res)))
    else:
        res = []
print(mx)
# 189
