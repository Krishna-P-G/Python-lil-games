from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)

    def next_level(self):
        self.goto(STARTING_POSITION)