xs = [int(x) for x in open("17.txt")]
ans = []
for i in range(len(xs) - 1):
  if ((xs[i] + xs[i + 1]) % 3 == 0 and (xs[i] + xs[i + 1]) % 6 != 0) and abs((xs[i] * xs[i + 1])) % 10 == 8):
    ans.append(xs[i] + xs[i + 1])
print(len(ans), max(ans))
