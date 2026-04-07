import turtle, time, user, scoreboard, cars, random

player1 = user.Player()
scoreboard.score()
active_cars = [cars.Car()]
game_on = True

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("The turtle vs 460")
screen.listen()
screen.onkeypress(user.move, "Up")
screen.onkeyrelease(user.stop, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()
    spawn_car = random.randint(1, 10)

    if user.walk:
        player1.forward()

    if player1.character.ycor() > 260:
        player1.reset()

    if spawn_car > 9:
        active_cars.append(cars.Car())
        if len(active_cars) > 2:
            if active_cars[-2].Car.distance(active_cars[-1].Car) <= 100:
                active_cars[-1].hide()
                active_cars.remove(active_cars[-1])

    for car in active_cars:
        if len(active_cars) > 0:
            car.forward()

        if car.Car.distance(player1.character) < 20:
            scoreboard.current_lives -= 1
            scoreboard.score()
            player1.clear()
            if scoreboard.current_lives == 0:
                game_on = False
                scoreboard.lives.teleport(0, 160)
                scoreboard.lives.write(f"Game Over!\nYou made it to level {scoreboard.current_level}!", font=("Times New Roman", 40, "bold"), align="center")

        if car.Car.xcor() < -400:
            car.hide()
            active_cars.remove(car)

screen.exitonclick()