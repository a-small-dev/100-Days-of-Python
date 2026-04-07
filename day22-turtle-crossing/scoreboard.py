import turtle

level, lives = turtle.Turtle(), turtle.Turtle()

current_level = 1
current_lives = 3

def score():

    level.ht()
    level.penup()
    level.teleport(x=-380, y=260)
    level.clear()
    level.pencolor("white")
    level.write(f"Level: {current_level}", font=("Times New Roman", 20, "bold",))

    lives.ht()
    lives.penup()
    lives.teleport(x=240, y=260)
    lives.clear()
    lives.pencolor("white")
    lives.write(f"Lives left: {current_lives}", font=("Times New Roman", 20, "bold"))