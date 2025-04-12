with open("26.txt") as f:
  n = int(f.readline())
  fst, snd, trd, fth = map(int, f.readline().split())
  bSts = []
  gSts = []
  for s in f:
    bads = 0
    xs = [int(x) for x in s.split()]
    if xs[1] < fst: bads += 1
    if xs[2] < snd: bads += 1
    if xs[3] < trd: bads += 1
    if xs[4] < fth: bads += 1
    if bads == 0: 
      xs += [sum(xs) - xs[0]]
      gSts.append(xs)
    else:
      xs += [sum(xs) - xs[0]]
      xs += [bads]
      bSts.append(xs)
gSts.sort(key = lambda x: (-x[5], x[0]))
bSts.sort(key = lambda x: (x[6], -x[5], x[0]))
for xs in bSts:
  if xs[-1] == 4:
    print(xs[0]) # второй ответ
    break
print(gSts[-1][0]) # первый ответ
