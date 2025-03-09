from re import *

s = open("24.txt").readline()

# третья задача
reg = r'(AA|BB)+'
reg = rf'(?=({reg}))'

print(max([len(x.group(1)) // 2 for x in finditer(reg, s)]))

# четвертая задача
reg = r'([123][ABC][123])+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) // 3 for x in finditer(reg, s)]))

# пятая задача
reg = r'(YZZ|XY|YZ)+'
reg = rf'(?=({reg}))'
print(max([len(x.group(1)) for x in finditer(reg, s)]))
