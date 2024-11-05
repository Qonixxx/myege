'''
Текстовый файл состоит из символов A, B, C, D и O. Определите максимальное количество идущих подряд пар символов вида согласная + гласная
'''

s = open("24_4602.txt").readline()
s = s.replace("O", "A").replace("C", "B").replace("D", "B")
s = s.replace("BA", "*")
s = s.replace("A", " ").replace("B", " ")
print(max(len(c) for c in s.split()))
