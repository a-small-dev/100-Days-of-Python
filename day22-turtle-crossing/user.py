import turtle, scoreboard, cars
PLAYER_SPEED = 10
PLAYER_STARTING_POSITION = (0.0, -280.0)
PLAYER_LIVES = 3

walk = False

def move():
    global walk
    walk = True

def stop():
    global walk
    walk = False


class Player:
    def __init__(self):
        self.lives = PLAYER_LIVES
        self.speed = PLAYER_SPEED
        self.character = turtle.Turtle()
        self.character.speed(self.speed)
        self.character.penup()
        self.character.shape("turtle")
        self.character.color("green")
        self.character.teleport(x=PLAYER_STARTING_POSITION[0], y=PLAYER_STARTING_POSITION[1])
        self.character.setheading(90)

    def forward(self):
        self.character.forward(PLAYER_SPEED)

    def reset(self):
        self.character.teleport(x=PLAYER_STARTING_POSITION[0], y=PLAYER_STARTING_POSITION[1])
        scoreboard.current_level += 1
        scoreboard.score()
        cars.current_level += 1

    def clear(self):
        self.character.teleport(x=PLAYER_STARTING_POSITION[0], y=PLAYER_STARTING_POSITION[1])
