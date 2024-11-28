s = "4" * 50

while "444" in s or "333" in s:
  if "444" in s: s = s.replace("444", "3", 1)
  else: s = s.replace("333", "3344", 1)
  if "3443" in s: s = s.replace("3443", "0", 1)

print(s)
