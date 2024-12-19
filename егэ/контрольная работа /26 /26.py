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
