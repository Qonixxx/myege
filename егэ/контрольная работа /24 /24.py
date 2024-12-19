s = open("24.txt").readline()
while "12" in s or "13" in s or "21" in s or "31" in s: s = s.replace("12", "1 2").replace("13", "1 3").replace("21", "2 1").replace("31", "3 1")
print(max(len(c) for c in s.split()))
