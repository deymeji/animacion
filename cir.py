import turtle as t
import colorsys as ca

t.bgcolor("black")
t.tracer(100)
h=0.2

def design():
    global h
    for i in range (4):
        for i in range (4):
            color = ca.hsv_to_rgb(h,1,1)
            h += 0.002
            t.fillcolor(color)
            t.begin_fill()
            t.fd(10)
            t.rt(80)
            t.fd(150)
            t.lt(12)
            t.end_fill()

for j in range(400):
    design()
    t.goto(8,8)
    t.rt(18)
t.done()