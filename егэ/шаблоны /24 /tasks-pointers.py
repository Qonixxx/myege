# два указателя

# AF более 200 раз

s = open('24.txt').readline()

TARGET = 201

s = s.replace('AF', '*').split('*')
s = s[1:-1]

minLen = float('inf')
for i in range(len(s)-TARGET+2):
  chunk = ''.join(s[i:i+TARGET-1])
  minLen = min( minLen, len(chunk) )

print( minLen + len('AF')*TARGET )

#-------------------------------------

s = open('24.txt').readline()

N = len(s)

R = 1
countAF = 0
minLen = float('inf')
for L in range(1,N):
  if s[L-1] == 'A' and s[L] == 'F':
    countAF -= 1
  while R < N and countAF < TARGET:
    R += 1
    if s[R-2] == 'A' and s[R-1] == 'F':
      countAF += 1
  if R >= N:
    break
  minLen = min( minLen, R-L )

print( minLen )


# '------------------------------------------------------------------------------------------------'

# CD равно 200 раз

s = open('24.txt').readline()

TARGET = 160

maxLen = 0
L = 0
countCD = 0
for R in range(len(s)):
  if s[R] == 'D' and R > 0 and s[R-1] == 'C':
    countCD += 1
  while countCD > TARGET:
    if s[L] == 'C' and s[L+1] == 'D':
      countCD -= 1
    L += 1
  if countCD == TARGET:
    maxLen = max( maxLen, R-L+1 )

print( maxLen )

#------------------------------------------

s = open('24-296.txt').readline()

s = s.replace('CD', 'C D').split()

maxLen = 0
for i in range(len(s)):
  chunk = ''.join(s[i:i + TARGET + 1])
  maxLen = max( maxLen, len(chunk) )

print( maxLen )

#---------------------------------------------------------------------------------------------

# не более 240 раз
s = open('24.txt').readline()

MAX = 240

maxLen = 0
L = 0
countDE = 0
for R in range(len(s)):
  if s[R] == 'E' and R > 0 and s[R-1] == 'D':
    countDE += 1
  while countDE > MAX:
    if s[L] == 'D' and s[L+1] == 'E':
      countDE -= 1
    L += 1
  maxLen = max( maxLen, R-L+1 )

print( maxLen )

#------------------------------------------

s = open('24-295.txt').readline()

s = s.replace('DE', 'D E').split()

maxLen = 0
for i in range(len(s)):
  chunk = ''.join(s[i:i + MAX + 1])
  maxLen = max( maxLen, len(chunk) )

print( maxLen )

