from turtle import*
a=["aqua","white", "mediumpurple"]
import time as t

speed(0)
pensize(3)
bgcolor("black")

def des1():
    for i in range (45):
        pencolor(a[i%3])
        circle(20,4)
        circle(150,180)
        pu()
        circle(150,180)
        pd()
    circle(150,180)


def des2():
    for i in range (45):
        pencolor(a[i%3])
        circle(-20,4)
        circle(-150,180)
        pu()
        circle(-150,180)
        pd()
pu()
goto(0,400)
pd()
des1()
des2()
des1()
des2()
t.sleep(10)
done()




