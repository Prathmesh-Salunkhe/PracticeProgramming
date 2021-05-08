#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Bazinga
#
# Created:     17-11-2018
# Copyright:   (c) Bazinga 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle as t
t.speed(0)

def face():
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.forward(5)
    for i in range(180):
        t.forward(1)
        t.left(1)

    t.forward(10)

    for i in range(180):
        t.forward(1)
        t.left(1)

    t.forward(5)
    t.end_fill()

    t.color("white")
    t.begin_fill()
    t.circle(53)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.circle(53)
    t.color("white")
    t.begin_fill()
    t.penup()
    t.setposition(-11,90)
    t.pendown()
    t.circle(11)
    t.forward(5)
    t.penup()
    t.setposition(11,90)
    t.pendown()
    t.circle(11)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setposition(-11,90)
    t.pendown()
    t.circle(11)
    t.forward(5)
    t.penup()
    t.setposition(11,90)
    t.pendown()
    t.circle(11)
    t.penup()
    t.setposition(9,100)
    t.pendown()
    t.pensize(5)
    t.circle(1)
    t.penup()
    t.setposition(-9,100)
    t.pendown()
    t.circle(1)
    t.pensize(1)
    t.color("red")
    t.begin_fill()
    t.penup()
    t.setposition(0,85)
    t.pendown()
    t.circle(5)
    t.end_fill()
    t.color("black")
    t.circle(5)
    t.right(90)
    t.forward(60)
    t.left(90)

    for i in range(38):
        t.left(1)
        t.forward(1)

    t.penup()
    t.setposition(0,25)
    t.pendown()
    t.right(38)
    t.right(180)

    for i in range(38):
        t.right(1)
        t.forward(1)

    t.left(38)
    t.right(180)
    t.penup()
    t.setposition(11,65)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setposition(9,75)
    t.pendown()
    t.left(30)
    t.forward(40)
    t.penup()
    t.setposition(9,55)
    t.pendown()
    t.right(60)
    t.forward(40)
    t.left(30)
    t.left(180)
    t.penup()
    t.setposition(-11,65)
    t.pendown()
    t.forward(40)
    t.penup()
    t.setposition(-9,75)
    t.pendown()
    t.right(30)
    t.forward(40)
    t.penup()
    t.setposition(-9,55)
    t.pendown()
    t.left(60)
    t.forward(40)
    t.right(30)
    t.left(180)
    t.penup()
    t.setposition(0,0)
    t.forward
    t.pendown()
    t.penup()
    t.setposition(-42,15)
    t.pendown()


def band():
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.left(1)

    t.right(50)
    t.right(90)
    t.forward(7)
    t.right(40)

    for i in range(50):
        t.right(1)
        t.forward(1)

    t.forward(10)

    for i in range(50):
        t.forward(1)
        t.right(1)

    t.right(40)
    t.forward(7)
    t.right(140)

    for i in range(50):
        t.left(1)
        t.forward(1)

    t.forward(5)
    t.end_fill()
    t.color("black")
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.left(1)

    t.right(50)
    t.right(90)
    t.forward(7)
    t.right(40)

    for i in range(50):
        t.right(1)
        t.forward(1)

    t.forward(10)

    for i in range(50):
        t.forward(1)
        t.right(1)

    t.right(40)
    t.forward(7)
    t.right(140)

    for i in range(50):
        t.left(1)
        t.forward(1)

    t.forward(5)


def bell():
    t.penup()
    t.setposition(0,0)
    t.pendown()
    t.right(180)
    t.color("yellow")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("black")
    t.circle(10)
    t.penup()
    t.setposition(0,-20)
    t.pendown()
    t.right(90)
    t.forward(8)
    t.right(90)
    t.color("grey")
    t.begin_fill()
    t.circle(4)
    t.end_fill()
    t.color("black")
    t.circle(4)

def lower():
    #right
    t.color("blue")
    t.begin_fill()
    t.penup()
    t.setposition(0,0)
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.left(1)

    t.right(50)
    t.right(90)
    t.forward(7)
    t.left(90)
    t.pendown()
    t.right(40)
    for i in range(55):
        t.forward(1)
        t.right(0.4)
    t.right(118)
    t.circle(10)
    t.circle(10,90)
    t.right(125)
    for i in range(30):
        t.forward(1)
        t.right(0.4)
    t.left(12)
    t.left(125)
    t.forward(16)
    for i in range(60):
        t.right(0.4)
        t.forward(1)
    t.left(24)
    t.right(90)
    t.forward(24)
    t.right(60)
    for i in range(40):
        t.right(0.4)
        t.forward(1)
    t.left(16)
    t.left(60)
    t.end_fill()

    #left

    t.begin_fill()
    t.penup()
    t.setposition(0,0)
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.right(1)

    t.left(50)
    t.left(90)
    t.forward(7)
    t.right(90)
    t.pendown()
    t.left(40)
    for i in range(55):
        t.forward(1)
        t.left(0.4)
    t.left(118)
    t.left(180)
    t.circle(10)
    t.circle(10,270)
    t.left(180)
    t.left(125)
    for i in range(30):
        t.forward(1)
        t.left(0.4)
    t.right(12)
    t.right(125)
    t.forward(16)
    for i in range(60):
        t.left(0.4)
        t.forward(1)
    t.right(24)
    t.left(90)
    t.forward(24)
    t.left(60)
    for i in range(40):
        t.left(0.4)
        t.forward(1)
    t.right(16)
    t.right(60)
    t.end_fill()

    #outline
    t.color("black")
    t.penup()
    t.setposition(0,0)
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.left(1)

    t.right(50)
    t.right(90)
    t.forward(7)
    t.left(90)
    t.pendown()
    t.right(40)
    for i in range(55):
        t.forward(1)
        t.right(0.4)
    t.right(118)
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("black")
    t.circle(10)
    t.circle(10,90)
    t.right(125)
    for i in range(30):
        t.forward(1)
        t.right(0.4)
    t.left(12)
    t.left(125)
    t.forward(16)
    for i in range(60):
        t.right(0.4)
        t.forward(1)
    t.left(24)
    t.right(90)
    t.forward(24)
    t.right(60)
    for i in range(40):
        t.right(0.4)
        t.forward(1)
    t.left(16)
    t.left(60)

    #left

    t.penup()
    t.setposition(0,0)
    t.forward(5)

    for i in range(50):
        t.forward(1)
        t.right(1)

    t.left(50)
    t.left(90)
    t.forward(7)
    t.right(90)
    t.pendown()
    t.left(40)
    for i in range(55):
        t.forward(1)
        t.left(0.4)
    t.left(118)
    t.left(180)
    t.color("white")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("black")
    t.circle(10)
    t.circle(10,270)
    t.left(180)
    t.left(125)
    for i in range(30):
        t.forward(1)
        t.left(0.4)
    t.right(12)
    t.right(125)
    t.forward(16)
    for i in range(60):
        t.left(0.4)
        t.forward(1)
    t.right(24)
    t.left(90)
    t.forward(24)
    t.left(60)
    for i in range(40):
        t.left(0.4)
        t.forward(1)
    t.right(16)
    t.right(60)

def foot():
    t.penup()
    t.setposition(40,-108)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(10,180)
    t.forward(25)
    t.circle(10,180)
    t.forward(25)
    t.penup()
    t.setposition(-15,-108)
    t.pendown()
    t.circle(10,180)
    t.forward(25)
    t.circle(10,180)
    t.forward(25)
    t.end_fill()

    t.color("black")
    t.penup()
    t.setposition(40,-108)
    t.pendown()
    t.circle(10,180)
    t.forward(25)
    t.circle(10,180)
    t.forward(25)
    t.penup()
    t.setposition(-15,-108)
    t.pendown()
    t.circle(10,180)
    t.forward(25)
    t.circle(10,180)
    t.forward(25)

def stomach():
    t.color("white")
    t.begin_fill()
    t.penup()
    t.setposition(0,-55)
    t.pendown()
    for i in range(40):
        t.left(1.5)
        t.forward(1)
    for i in range(40):
        t.left(1)
        t.forward(1)
    t.right(40*1.5+40)
    t.right(180)
    t.forward(11)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(28)
    t.penup()
    t.setposition(0,-55)
    t.pendown()
    for i in range(40):
        t.right(1.5)
        t.forward(1)
    for i in range(40):
        t.right(1)
        t.forward(1)
    t.left(40*1.5+40)
    t.left(180)
    t.forward(11)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(28)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setposition(0,-55)
    t.pendown()
    for i in range(40):
        t.left(1.5)
        t.forward(1)
    for i in range(40):
        t.left(1)
        t.forward(1)
    t.right(40*1.5+40)
    t.right(180)
    t.forward(11)
    t.left(90)
    t.forward(5)
    t.right(90)
    t.forward(28)
    t.penup()
    t.setposition(0,-55)
    t.pendown()
    for i in range(40):
        t.right(1.5)
        t.forward(1)
    for i in range(40):
        t.right(1)
        t.forward(1)
    t.left(40*1.5+40)
    t.left(180)
    t.forward(11)
    t.right(90)
    t.forward(5)
    t.left(90)
    t.forward(28)

def pocket():
    t.color("black")
    t.penup()
    t.setposition(0,-50)
    t.pendown()
    t.circle(25,90)
    t.penup()
    t.setposition(0,-50)
    t.pendown()
    t.right(90)
    t.circle(25,-90)
    t.left(90)
    t.forward(50)
    wait=input()



face()
lower()
stomach()
band()
foot()
bell()
pocket()