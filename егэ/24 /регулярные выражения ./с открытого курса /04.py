# арифметические выражения

from re import *
s = open('24.txt').readline()

# шестая задача

num = r'([1-9][0-9]*)'
reg = rf'{num}([*-]{num})+'

m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)

# седьмая задача

num = r'[12][012]*|0'
reg = rf'{num}([+*]{num})*'

m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)

# проверка

# print(s[:50])
# print([x.group() for x in finditer(num, s)])
