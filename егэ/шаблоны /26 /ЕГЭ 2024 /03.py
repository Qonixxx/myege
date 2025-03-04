'''
В магазине продаётся N товаров нескольких артикулов. Товары одного артикула имеют одинаковую цену. 
Учёт товаров ведётся поштучно, для каждой единицы товара известен её текущий статус (продана или нет). 
Товары разделены на две категории: дорогие и дешёвые.
 Дорогими считаются товары, цена на которые превышает среднюю цену (среднее арифметическое) всех товаров в базе данных магазина без учёта их текущего статуса, 
остальные товары считаются дешёвыми. Лидером продаж называется товар с таким артикулом, наибольшее количество единиц которого продано. 
Лидер продаж выбирается среди дорогих товаров, а если продано одинаковое количество дорогих товаров с разными артикулами, 
лидером выбирается товар с наибольшей ценой. Если и таких товаров несколько, лидер продаж – тот из них, которого осталось меньше всего. 
Найдите суммарную стоимость оставшихся единиц товара – лидера продаж, а также артикул этого товара.
'''

with open('26-153.txt') as F:
  N = int(F.readline())
  data = {}
  for i in range(N):
    art, price, status = map( int, F.readline().split() )
    artData = data.get( art, (price, 0, 0) )
    data[art] = (price, artData[1]+status, artData[2]+1-status)

# Средняя цена по всем товарам
sumPrice, count = 0, 0
for d in data.values():
  count += d[1]+d[2]
  sumPrice += (d[1]+d[2])*d[0]
avgPrice = sumPrice / count

# Дорогие товары
data = [ (art, *d) for art, d in data.items()
                   if d[0] > avgPrice ]

data.sort( key = lambda x: (
                 -x[3],  # продано больше всего
                 -x[1],  # наибольшая цена
                  x[2]   # осталось меньше всего
    ) )

print( data[0][1]*data[0][2], data[0][0] )
