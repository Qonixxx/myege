'''
Определите количество 15-ричных пятизначных чисел, в записи которых ровно одна цифра 8 и не менее двух цифр с числовым значением, превышающим 9.
'''

from itertools import *
k = 0

for x in product("0123456789abcde", repeat = 5):
    s = "".join(x)
    if s.count("8") == 1 and s[0] != "0" and s.count("a") + s.count("b") \
       + s.count("c") + s.count("d") + s.count("e") >= 2:
        k += 1
print(k)
# ans - 83175
