'''
В файле записана последовательность символов, 
состоящей из строчных латинских букв и цифр. 
Укажите длину самой длинной последовательности, состоящей из цифр. 
'''

s = open("24.txt").readline()
for c in "qwertyuiopasdfghjklzxcvbnm":
  s = s.replace(c, " ")
print(max(len(c) for c in s.split()))
