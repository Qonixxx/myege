from turtle import *
tracer(0)
screensize(5000, 5000)
r = 15

for i in range(9):
    fd(27 * r)
    rt(90)
    fd(30 * r)
    rt(90)
up()
fd(3 * r)
rt(90)
fd(6 * r)
lt(90)
down()
for i in range(9):
    fd(77 * r)
    rt(90)
    fd(66 * r)
    rt(90)
up()

for x in range(-99, 99):
    for y in range(-99, 99):
        goto(x * r, y * r)
        dot(3, "blue")
update()
