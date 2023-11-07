import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.add_food()

    def add_food(self):
        self.clear()
        x, y = random.randint(-280, 280), random.randint(-280, 280)
        self.goto(x, y)
