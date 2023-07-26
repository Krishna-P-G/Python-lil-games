import random
from turtle import Turtle


class Bomb(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1.5, stretch_wid=1.5)
        self.color("red")
        self.speed("fastest")
        self.bomb_refresh()

    def bomb_refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # # Check if the new position overlaps with the food
        # while self.distance(food) < 20:
        #     random_x = random.randint(-280, 280)
        #     random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)
