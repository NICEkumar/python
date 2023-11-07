from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def win(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER \n LEVEL : {self.level}", align="center",font=FONT)