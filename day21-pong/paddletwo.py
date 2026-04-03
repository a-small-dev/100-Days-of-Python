import turtle
paddletwo = turtle.Turtle()

def usertwo():
    paddletwo.shape("square")
    paddletwo.color("white")
    paddletwo.tilt(90)
    paddletwo.penup()
    paddletwo.shapesize(stretch_wid=1, stretch_len=5)
    paddletwo.teleport(-350, 0)

def moveup():
    paddley = paddletwo.ycor()
    if paddley < 250:
        paddletwo.sety(paddley + 5)

def movedown():
    paddley = paddletwo.ycor()
    if paddley > -250:
        paddletwo.sety(paddley - 5)