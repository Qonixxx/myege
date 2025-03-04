'''
На производстве штучных изделий N деталей должны быть отшлифованы и окрашены. Для каждой детали известно время её шлифовки и время окрашивания. 
Детали пронумерованы начиная с единицы. Параллельная обработка деталей не предусмотрена. На ленте транспортёра имеется N мест для каждой из N деталей. 
На ленте транспортёра детали располагают по следующему алгоритму:
–	все 2N чисел, обозначающих время окрашивания и шлифовки для N деталей, упорядочивают по возрастанию;
–	если минимальное число в этом упорядоченном списке – это время шлифовки конкретной детали, то деталь размещают на ленте транспортёра на первое свободное место от её начала;
– если минимальное число – это время окрашивания, то деталь размещают на первое свободное место от конца ленты транспортёра
– если число обозначает время окрашивания или шлифовки уже рассмотренной детали, то его не принимают во внимание.
Этот алгоритм применяется последовательно для размещения всех N деталей. 
Определите номер последней детали, для которой будет определено её место на ленте транспортёра, и количество деталей, которые будут отшлифованы до неё.
'''

with open("26.txt") as f:
    N = int(f.readline())
    details = []
    for i in range(N):
        sl, pkr = map(int, f.readline().split())
        if sl < pkr: details.append([sl, "sl", i + 1]) # if sanding time is less than painting time, then add the time, type and part number
        else: details.append([pkr, "pkr", i + 1])
    details.sort()
    
    # to store answers
    last = 0
    ksl = kpkr = last_sl = last_pkr = 0
    
    overall = [0] * N
    for i in range(N):
        time, tp, number = details[i]
        if tp == "sl":
            for j in range(N):
                if overall[j] == 0: 
                    overall[j] = 1 # if the space on the tape is free, then place the part
                    last = number
                    last_sl = ksl
                    ksl += 1
                    break
        else:
            for j in reversed(range(N)):
                if overall[j] == 0:
                    overall[j] = 1 # similarly
                    last = number
#                    last_pkr = kpkr
#                    kpkr += 1
                    break
print(last, last_sl) # 732 497


# print(last_sl + last_pkr)
