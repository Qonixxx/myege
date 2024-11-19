'''
Сколько существует чисел, девятеричная запись которых состоит из шести цифр,
не начинается с нечётных цифр, не оканчивается цифрами 2 и 3 и содержит не менее двух цифр 1?
'''

from itertools import *
k = 0

for x in product("012345678", repeat = 6):
    s = "".join(x)
    if s.count("1") >= 2 and s[0] != "0" and s[-1] != "2" and s[-1] != "3" \
       and int(s[0]) % 2 == 0:
        k += 1
print(k)
# ans - 19868
