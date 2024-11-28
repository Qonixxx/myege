from turtle import *

tracer(0)
r = 50

for i in range(5):
  fd(35 * r)
  rt(90)
  fd(24 * r)
  rt(90)
up()
rt(90)
fd(7 * r)
rt(90)
fd(5 * r)
down()
for i in range(1001):
  rt(90)
  fd(20 * r)
  rt(90)
  fd(36 * r)
up()
for x in range(-60, 60):
  for y in range(-60, 60):
    goto(x * r, y * r)
    dot(3, "blue")
update()
  
