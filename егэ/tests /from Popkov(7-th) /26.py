with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([int(x) for x in f], reverse = True)
    # для первого ответа - True, для второго - False

discount = n // 4    
for i in range(discount):
    xs[i] = xs[i] / 2
print(sum(xs))
