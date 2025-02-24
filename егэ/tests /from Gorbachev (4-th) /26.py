with open("26.txt") as f:
    n = int(f.readline())
    xs = sorted([int(x) for x in f], reverse = True)
    
# для первого ответа

'''
discount = n // 5
for i in range(discount):
    xs[i] = xs[i] / 2
print(sum(xs))
'''

# второй ответ
'''
for i in range(0, n, 5):
    xs[i] = xs[i] / 2
print(sum(xs))
'''

# 40931712 44876714
