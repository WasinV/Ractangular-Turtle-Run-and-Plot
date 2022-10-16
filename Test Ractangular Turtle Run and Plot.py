import sys
print(sys.version)

import turtle
tao = turtle.Pen() #ดึงปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า

def Rectangle():
    '''วาดสี่เหลี่ยม'''
    for i in range(4):
        tao.forward(200)
        tao.left(90)

def Go(x,y):
    '''ไปที่ชอบ'''
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def Circle():
    '''วาดวงกลม'''
    for i in range(10):
        tao.circle(50)
        tao.left(36)

Go(-100,-100)
Rectangle()

Go(100,100)
Circle()
Go(-100,100)
Circle()
Go(100,-100)
Circle()
Go(-100,-100)
Circle()
