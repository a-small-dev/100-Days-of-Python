import gameball, turtle, paddleone, paddletwo, time, score, input_handler as i

game = True

screen = turtle.Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

paddleone.userone()
paddletwo.usertwo()
score.scoreboard()

for x in range(20):
    score.seperate()

screen.listen()

screen.onkeypress(i.up_press, "Up")
screen.onkeyrelease(i.up_release, "Up")

screen.onkeypress(i.down_press, "Down")
screen.onkeyrelease(i.down_release, "Down")

screen.onkeypress(i.w_press, "w")
screen.onkeyrelease(i.w_release, "w")

screen.onkeypress(i.s_press, "s")
screen.onkeyrelease(i.s_release, "s")

while game:
    screen.update()
    gameball.move()

    if gameball.ball.ycor() > 280 or gameball.ball.ycor() < -280:
        gameball.ball.setheading(-gameball.ball.heading())

    if (340 < gameball.ball.xcor() < 350) and \
        (paddleone.paddleone.ycor() + 50 > gameball.ball.ycor() > paddleone.paddleone.ycor() - 50):
        gameball.ball.setx(340)
        gameball.ball.setheading(180 - gameball.ball.heading())

    if (-340 > gameball.ball.xcor() > -350) and \
        (paddletwo.paddletwo.ycor() + 50 > gameball.ball.ycor() > paddletwo.paddletwo.ycor() - 50):
        gameball.ball.setx(-340)
        gameball.ball.setheading(180 - gameball.ball.heading())

    if gameball.ball.xcor() < -360:
        gameball.ball.teleport(x=0, y=0)
        score.user2_scored()
        gameball.ball_speed = 3.0
        score.scoreboard()

    if gameball.ball.xcor() > 360:
        gameball.ball.teleport(x=0, y=0)
        score.user1_scored()
        gameball.ball_speed = 3.0
        score.scoreboard()

    if score.user1_score == 3:
        gameball.ball.hideturtle()
        paddletwo.paddletwo.hideturtle()
        paddleone.paddleone.hideturtle()
        score.user1_scoreboard.color("green")
        score.user2_scoreboard.color("red")
        score.user1_scoreboard.teleport(x=0, y=0)
        score.user1_scoreboard.write("Player 1 Wins!", align="center", font=("Courier", 48, "bold"))
        game = False
        screen.exitonclick()

    if score.user2_score == 3:
        gameball.ball.hideturtle()
        paddletwo.paddletwo.hideturtle()
        paddleone.paddleone.hideturtle()
        score.user1_scoreboard.color("green")
        score.user2_scoreboard.color("red")
        score.user1_scoreboard.teleport(x=0, y=0)
        score.user1_scoreboard.write("Player 2 Wins!", align="center", font=("Courier", 48, "bold"))
        game = False
        screen.exitonclick()

    if i.up_pressed:
        paddleone.moveup()
    if i.down_pressed:
        paddleone.movedown()

    if i.w_pressed:
        paddletwo.moveup()
    if i.s_pressed:
        paddletwo.movedown()
    time.sleep(0.01)