import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossy road")
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player_turtle = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player_turtle.go_up, "Up")
screen.onkeypress(player_turtle.go_down, "Down")

counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_forward()

    """The turtle touches finish line"""
    if player_turtle.ycor() > 280:
        player_turtle.next_level()
        scoreboard.increase_level()
        car_manager.speed_up()

    """The turtle collides with the car"""
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    counter += 1

screen.exitonclick()