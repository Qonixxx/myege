'''
Система наблюдения ежеминутно фиксирует вход и выход посетителей магазина (в минутах, прошедших от начала суток). 
Считается, что в минуты фиксации входа и выхода посетитель находится в магазине. Нулевая минута соответствует моменту открытия магазина, 
который работает 24 ч в сутки без перерыва. Менеджер магазина анализирует данные системы наблюдения за прошедшие сутки, 
и выявляет отрезки времени наибольшей длины, в течение которых число посетителей, находящихся в магазине, не изменялось. 
Далее менеджер выбирает пики посещаемости – промежутки времени, когда количество посетителей в магазине было наибольшим. Пиков посещаемости в течение суток может быть несколько.
'''

with open('26-130.txt') as F:
  N = int(F.readline())
  count = [0] * 1440
  for i in range(N):
    t1, t2  = map(int, F.readline().split())
    for t in range(t1, t2+1):
      count[t] += 1

peakValue = max(count)

numPeaks = 0
for i in range(1,1440):
  if count[i] == peakValue and count[i] > count[i-1]:
    numPeaks += 1

print( numPeaks, peakValue  )

