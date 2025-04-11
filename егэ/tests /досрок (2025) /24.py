from re import *
s = open("24.txt").readline()
reg = r"[1-B][0-B]*[02468A]"
m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)
