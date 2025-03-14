'''
Отбор кандидатов в матросы происходит по сумме баллов трех экзаменов. 
На заранее известное количество мест отбираются кандидаты, набравшие большую сумму баллов по результатам трех экзаменов. 
Все кандидаты, набравшие определенную сумму баллов или больше, зачисляются на имеющиеся места. Такой балл называется проходным. 
Если после заполнения имеющихся мест кандидатами с проходным баллом остаются незаполненные места, но кандидатов, набравших следующую сумму баллов, 
больше чем вакантных мест, набранная этими кандидатами сумма баллов называется полупроходным баллом. Из числа кандидатов, набравших полупроходной балл, 
на имеющиеся места принимаются кандидаты, имеющие более высокий балл за собеседование, а при равенстве баллов за собеседование – приоритет имеют кандидаты с наименьшими ID. 
Для данного множества кандидатов определите ID последнего кандидата с набранным проходным баллом, а также количество кандидатов, набравших полупроходной балл.
'''

with open('26.txt') as F:
  N, S = [int(x) for x in F.readline().split()]
  data = []
  for i in range(N):
    ID, o1, o2, o3, sobes = map( int, F.readline().split() )
    data.append( (o1+o2+o3, sobes, -ID) )

data.sort( reverse = True )
# print(data)

last = data[S-1]
print( last )
if last[0] > data[S][0]: # нет полупроходного балла
  print( -last[2], 0 )
else:
  halfPass = last[0]
  iLastPass = S - 2
  while data[iLastPass][0] == last[0]:
    iLastPass -= 1
  print( -data[iLastPass][2],
         len([ d for d in data if d[0] == halfPass ] ) )
