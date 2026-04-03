import gameball, turtle as t

user1_score = 0
user2_score = 0
user1_scoreboard = t.Turtle()
user2_scoreboard = t.Turtle()

def seperate():
    seperator.forward(20)
    seperator.penup()
    seperator.forward(10)
    seperator.pendown()

seperator = t.Turtle()
seperator.pendown()
seperator.teleport(x=0, y=300)
seperator.hideturtle()
seperator.speed(10000)
seperator.pencolor("red")
seperator.setheading(270)


def scoreboard():
    user1_scoreboard.hideturtle()
    user2_scoreboard.hideturtle()
    user1_scoreboard.color("white")
    user2_scoreboard.color("white")
    user1_scoreboard.teleport(x=-55, y=210)
    user2_scoreboard.teleport(x=25, y=210)
    user1_scoreboard.clear()
    user2_scoreboard.clear()
    user1_scoreboard.write(user1_score, font=("Arial", 48, "bold"))
    user2_scoreboard.write(user2_score, font=("Arial", 48, "bold"))
    gameball.spawnball()

def user1_scored():
    global user1_score
    user1_score += 1

def user2_scored():
    global user2_score
    user2_score += 1
