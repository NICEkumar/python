import turtle
from turtle import Turtle,Screen
import random
tim = Turtle()
turtle.colormode(255)
tim.penup()
tim.speed("fastest")
tim.hideturtle()

color = [(202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156),
         (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126),
         (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24),
         (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)


def reset():
    tim.setheading(90)
    tim.fd(50)
    tim.left(90)
    tim.forward(500)
    tim.setheading((0))


for _ in range(1,101):
    tim.dot(20, random.choice(color))
    tim.fd(50)
    if _% 10 == 0:
        reset()





screen = Screen()
screen.exitonclick()
