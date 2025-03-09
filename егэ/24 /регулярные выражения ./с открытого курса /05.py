# легенда
from re import *

s = open('24.txt').readline()

num = r'([1-9][0-9]*|0)'
pr = rf'(({num}\*)*0(\*{num})*)'
reg = rf'{pr}(\+{pr})+'

m = max([x.group() for x in finditer(reg, s)], key = len)
print(len(m), m)
