import turtle
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
score = Scoreboard()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.add_food()
        snake.extend()
        score.increase_score()

    # collision with wall

    if snake.head.xcor() > 285 or snake.head.ycor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() < -285:
        gameOn = False
        score.game_over()

    # collision with tail

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            gameOn = False
            score.game_over()

screen.exitonclick()
