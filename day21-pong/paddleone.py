import turtle
paddleone = turtle.Turtle()

def userone():
    paddleone.shape("square")
    paddleone.color("white")
    paddleone.tilt(90)
    paddleone.penup()
    paddleone.shapesize(stretch_wid=1, stretch_len=5)
    paddleone.teleport(350, 0)

def moveup():
    paddley = paddleone.ycor()
    if paddley < 250:
        paddleone.sety(paddley + 5)

def movedown():
    paddley = paddleone.ycor()
    if paddley > -250:
        paddleone.sety(paddley - 5)