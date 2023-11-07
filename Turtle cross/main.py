import time
from turtle import Screen
from player import Player
from score import Score
from car_manager import CarManager


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = Score()
screen.listen()


def game():

    screen.onkey(player.go_up, "Up")
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        cars.create_car()
        cars.move_cars()

        for car in cars.all_cars:
            if car.distance(player) < 20:
                score.game_over()
                game_is_on = False

        if player.is_at_finish_line():
            score.win()
            cars.level_up()
            player.restart()


game()
screen.onkey(game, "Return")

screen.exitonclick()
