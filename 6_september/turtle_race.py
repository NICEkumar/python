from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
race_on = False
user_bet = screen.textinput("bet?", "who will win the race?:")

color = ["red", "blue", "green"]
y = [-100, 0, 100]
all_turtles = []


for i in range(3):
    new_player = Turtle(shape='turtle')
    new_player.penup()
    new_player.color(color[i])
    new_player.goto(-200, y[i])
    all_turtles.append(new_player)


if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            if turtle.pencolor() == user_bet:
                print("you won")
            else:
                print("you lost")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()

