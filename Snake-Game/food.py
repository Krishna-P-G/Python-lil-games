import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # # Check if the new position overlaps with the Bomb
        # while self.distance(bomb) < 20:
        #     random_x = random.randint(-280, 280)
        #     random_y = random.randint(-280, 280)

        self.goto(random_x, random_y)