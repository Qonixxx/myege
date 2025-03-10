'''
Текстовый файл состоит из символов, обозначающих буквы латинского алфавита А, В и С и цифры 8 и 9.

Определите в прилагаемом файле максимальное количество идущих подряд символов, среди которых ни одна буква не стоит рядом с буквой, а цифра — с цифрой.
'''

s = open("24.txt").readline()
s = s.replace("B", "A").replace("C", "A").replace("8", "9")
while "AA" in s: s = s.replace("AA", "A A")
while "99" in s: s = s.replace("99", "9 9")
print(max(len(c) for c in s.split()))
