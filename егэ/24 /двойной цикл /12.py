s = open("24.txt").readline()
m = 0

for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l:r + 1]
        if c.count("X") == 5 and c.count("Y") == 5 and c.count("Z") == 5:
            m = max(m, len(c))
        elif c.count("X") > 5 or c.count("Y") > 5 or c.count("Z") > 5:
            break
print(m)
# не пишется блок else: break, т.к кол-во букв может собраться в дальнейшем
