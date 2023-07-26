from turtle import Turtle


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.timer = 60
        self.update_time()

    def update_time(self):
        self.clear()
        self.goto(0, 290)
        self.write(self.timer, align="center", font=("Courier", 60, "normal"))

    def decrease_time(self):
        self.timer -= 1
        self.update_time()
