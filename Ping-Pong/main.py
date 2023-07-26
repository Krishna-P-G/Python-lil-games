from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard
from timer import Timer

screen = Screen()
screen.title("Ping pong")
screen.setup(width=1500, height=750)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((700, 0))
l_paddle = Paddle((-710, 0))
r_paddle.color("blue")
l_paddle.color("red")

ball = Ball()
ball.speed("fastest")
score = ScoreBoard()
timer = Timer()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

start_time = time.time()
pong_on = True
while pong_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    """Detect collision with walls on top and bottom / start to bounce"""
    if ball.ycor() > 350 or ball.ycor() < -350:
        ball.bounce_y()

    """Detect collision with paddles"""
    if ball.distance(r_paddle) < 50 and ball.xcor() > 600:
        ball.check_collision(r_paddle)
    if ball.distance(l_paddle) < 50 and ball.xcor() < -600:
        ball.check_collision(l_paddle)

    """Detect if bal goes out boundary"""
    if ball.xcor() > 720:
        ball.reset_ball()
        score.l_point()

    if ball.xcor() < -720:
        ball.reset_ball()
        score.r_point()

    elapsed_time = time.time() - start_time
    if elapsed_time >= 1:  # Decrease timer every second
        timer.decrease_time()
        start_time = time.time()

    if timer.timer == 0:
        pong_on = False
        if score.l_score > score.r_score:
            score.game_over_l()
        elif score.l_score < score.r_score:
            score.game_over_r()
        else:
            score.game_over()
screen.exitonclick()
