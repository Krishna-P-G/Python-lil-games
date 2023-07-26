import random
from turtle import Turtle
import random
MOVE = [10, -10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.choice(MOVE)
        self.y_move = random.choice(MOVE)
        self.move_speed = 0.1
        self.is_collided = False

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.reset_collision()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if not self.is_collided:
            self.x_move *= -1
            self.move_speed *= 0.8
            self.is_collided = True

    def reset_collision(self):
        self.is_collided = False

    def check_collision(self, paddle):
        if self.distance(paddle) < 50 and abs(self.xcor() - paddle.xcor()) < 20:
            self.bounce_x()

    def reset_ball(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()