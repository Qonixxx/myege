with open("9.txt") as f:
    k = 0
    for s in f:
        arr = [int(x) for x in s.split()]
        vector = [x for x in arr if 1 <= arr.count(x) <= 2]
        xs = set(vector)
        if len(xs) == 5 and ((sum(xs) / len(xs)) <= (sum(vector) / len(vector))):
            k += 1
            print(arr, xs)
print(k)
