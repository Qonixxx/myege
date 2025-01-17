base = ''

s = open(base + '24.txt').readline().strip()
pos = [-1]
i = 0
ls = len(s)
while i < ls:
    if s[i:i+4] == 'FSRQ':
        pos.append(i)
        i += 4
    else:
        i += 1
if pos[-1] + 4 != ls:
    pos.append(ls - 3)
mx = max([b + 2 - a for a, b in zip(pos, pos[81:])])
print(mx)
