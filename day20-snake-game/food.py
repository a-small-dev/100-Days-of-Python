from turtle import Turtle
import random

class Food:
    def __init__(self):
        self.pellets = []
        self.create_food()

    def random_coord(self):
        return random.randint(-250, 250), random.randint(-250, 250)

    def create_food(self):
        pellet = Turtle()
        pellet.color("purple")
        pellet.shape("circle")
        pellet.penup()
        pellet.teleport(self.random_coord()[0], self.random_coord()[1])
        self.pellets = pellet

