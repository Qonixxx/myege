'''
Текстовый файл состоит из символов A, B, C, D, E.

Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых символ A повторяется не более 3 раз
'''

s = open("24.txt").readline()
s = s.split("A")
mx = 0
for i in range(len(s) - 3): 
  c = "A".join(s[i:i+4])
  mx = max(len(c), mx)
print(mx)
