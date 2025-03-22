from math import *

data = []
for s in open("27_B.txt"):
  a, r = map(float, s.split())
  x = r * cos(radians(a))
  y = r * sin(radians(a))
  data.append([x, y])
print(len(data))

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def gkl(p0):
    kl = [p for p in data if dist(p0, p) < 2.5]
    if len(kl) > 0:
        for p in kl: data.remove(p)
        nkl = [gkl(p) for p in kl]
        for c in nkl: kl.extend(c)
    return kl

def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]

kls = []
while len(data) > 0:
  p0 = data.pop()
  kl = [p0] + gkl(p0)
  print(len(kl))
  kls.append(kl)
print(len(kls))

centrs = [center(kl) for kl in kls]
px = sum(x for x, y in centrs) / len(kls)
py = sum(y for x, y in centrs) / len(kls)
print(int(px * 10 ** 4), int(py * 10 ** 4)) 
