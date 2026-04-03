import random, turtle as t
global ball, ball_speed
ball = t.Turtle()
ball_speed = 3.0

def spawnball():
    directions = [45,135, 225, 315]
    ball.color("white")
    ball.shape("circle")
    ball.speed(10)
    ball.penup()
    ball.teleport(x=0, y=0)
    ball.setheading(random.choice(directions))

def move():
    global ball_speed
    ball.forward(ball_speed)
    ball_speed += 0.002
