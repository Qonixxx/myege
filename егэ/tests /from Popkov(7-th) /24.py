s = open("24.txt").readline()
s = s.replace("MA", "*").replace("XA", "*")
s = s.replace("M", " ").replace("A", " ").replace("X", " ")
print(max(len(c) for c in s.split()))
