from turtle import Screen, Turtle
from snake import Snake
from food import Food
from bomb import Bomb
from scoreboard import ScoreBoard

import time

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Snake Game in Moon")
screen.tracer(0)

snake = Snake()
bomb = Bomb()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """Detect collision with food"""
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

        """Refresh bomb position every time score increases by 2"""
        if scoreboard.score % 2 == 0:
            bomb.bomb_refresh()

    """Detect collision with bomb"""
    if snake.head.distance(bomb) < 15:
        scoreboard.reset()
        snake.reset()

    """Detect collision with wall"""
    if snake.head.xcor() > 380 or snake.head.xcor() < -400 or snake.head.ycor() > 340 or snake.head.ycor() < -350:
        scoreboard.reset()
        snake.reset()

    """Detect collision with tail"""
    for segment in snake.snakes:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
