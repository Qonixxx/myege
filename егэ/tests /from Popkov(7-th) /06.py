from turtle import *
tracer(0)
screensize(5000, 5000)
r = 20

for i in range(5):
    fd(7 * r)
    lt(90)
    fd(17 * r)
    lt(90)
up()
bk(1 * r)
lt(90)
fd(4 * r)
rt(90)
down()
for i in range(3):
    fd(14 * r)
    rt(90)
    fd(6 * r)
    rt(90)
up()

for x in range(-99, 99):
    for y in range(-99, 99):
        goto(x * r, y * r)
        dot(3, "red")
update()
