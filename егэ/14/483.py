'''
Значение арифметического выражения 6 ** 260 + 6 ** 160 + 6 ** 60 – х, 
где х – целое положительное число, не превышающее 2030,
записали в 6-ричной системе счисления. 
Определите наименьшее значение х, при котором количество нулей в 6-ричной записи числа,
являющегося значением данного арифметического выражения, равно 202. 
В ответе запишите число в десятичной системе счисления.
'''

def toBase(n, b):
  s = ''
  while n:
    s = str(n % b) + s
    n //= b
  return s

for x in range(1,2030):
  n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
  s = toBase(n, 6)
  if s.count('0') == 202:
    print(x)
    break
# ans - 216
