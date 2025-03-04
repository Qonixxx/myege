'''
Входной файл содержит сведения о заявках на проведение занятий в конференц-зале. 
В каждой заявке указаны время начала и время окончания мероприятия (в минутах от начала суток). 
Если время начала одного мероприятия меньше времени окончания другого, то провести можно только одно из них. 
Если время окончания одного мероприятия совпадает с временем начала другого, то провести можно оба. 
Определите максимальное количество мероприятий, которое можно провести в конференц-зале и самое позднее время окончания последнего мероприятия.
'''

with open('26.txt') as F:
  N = int(F.readline())
  data = []
  for _ in range(N):
    start, end  = map(int, F.readline().split())
    data.append( (start, end) )

data.sort( key = lambda x: x[1] ) # сортируем по времени окончания

allActions = []
for start, end in data:
  if not allActions or start >= allActions[-1]:
     allActions.append( end )

freeLast = 0
for start, end in data:
  if start >= allActions[-2]:
    freeLast = max( end, freeLast )

print( len(allActions), freeLast )
