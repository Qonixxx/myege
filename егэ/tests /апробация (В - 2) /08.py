from itertools import product
k = 0
for x in product('012345678', repeat = 5):
    s = ''.join(x)
    s = s.replace('3', '1').replace('5', '1').replace('7', '1')
    if s[0] != '0' and s.count('0') == 1 and '10' not in s and '01' not in s:
        k += 1
print(k)
# 5120
