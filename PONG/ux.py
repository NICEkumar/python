from turtle import Turtle


class Ux(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 300)
        self.setheading(270)
        for i in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.penup()
        self.goto(-400,300)
        self.pendown()
        self.hideturtle()
        self.pensize(15)
        self.setheading(0)
        self.forward(800)
        self.setheading(270)
        self.forward(600)
        self.setheading(180)
        self.forward(800)
        self.setheading(90)
        self.forward(600)