with open("9.txt") as f:
    k = 0
    for s in f:
        arr = sorted([int(x) for x in s.split()])
        if (len(arr) == len(set(arr))) and (((arr[0] + arr[3]) / 2) <= ((arr[2] + arr[3]) / 2)): k += 1
    print(k)
