'''
Значение арифметического выражения 5 ** 100 – х, где х – целое положительное число, превышающее 8300, 
записали в системе счисления с основанием 5
Определите наименьшее значение х, при котором в пятеричной записи числа, 
являющегося значением данного арифметического выражения, содержится ровно четыре нуля.

ответ в 10 СС
'''

for x in range(8300, 10000):
    res = 5 ** 100 - x
    xs = []
    while res:
        xs = [res % 5] + xs
        res //= 5
    if xs.count(0) == 4:
        print(x)
        break
# ответ - 8750
