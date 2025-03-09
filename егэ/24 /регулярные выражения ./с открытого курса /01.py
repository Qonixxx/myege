# первая задача с вебинара

from re import *
s = open("24.txt").readline()
reg = r'{ABC}+'

print(max([len(x.group()) for x in finditer(reg, s)]))

# для проверки регулярки

# print(s[:100])
# print([x.group() for x in finditer(reg, s[:100])])
