import turtle, random

current_level = 0
CAR_SPEED_INCREASE = 1.7
CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_X_POSITION = 400
CAR_SPEED = 5
CAR_SHAPE = "square"

class Car:
    def __init__(self):
        self.Car = turtle.Turtle()
        self.Car.shape(CAR_SHAPE)
        self.Car.shapesize(stretch_wid=None, stretch_len=2)
        self.Car.color(random.choice(CAR_COLORS))
        self.Car.penup()
        self.Car.setheading(180)
        self.Car.teleport(x=CAR_STARTING_X_POSITION, y=random.randint(-200, 200))

    def forward(self):
        self.Car.forward(CAR_SPEED + (CAR_SPEED_INCREASE * current_level))

    def hide(self):
        self.Car.ht()
        del self.Car
