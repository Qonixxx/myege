# вторая и третья задача вебинара
from re import *

# вторая задача
s = open("24.txt").readline()
reg = r'(ZX|ZY)+'
print(max([len(x.group()) // 2 for x in finditer(reg, s)])) # делим на 2, тк пара

# третья задача

reg = r'([BCD][AO])+'
print(max([len(x.group()) // 2 for x in finditer(reg, s)]))





