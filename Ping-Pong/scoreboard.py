from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 290)
        self.color("red")
        self.write(self.l_score, align="center", font=("Courier", 60, "normal"))
        self.goto(100, 290)
        self.color("blue")
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over_l(self):
        self.goto(0, 10)
        self.color("red")
        self.write(f"GAME OVER", align="center", font=("Courier", 60, "normal"))
        self.goto(0, -60)
        self.color("red")
        self.write(f"THE RED TEAM WINS", align="center", font=("Courier", 40, "normal"))

    def game_over_r(self):
        self.goto(0, 10)
        self.color("blue")
        self.write(f"GAME OVER", align="center", font=("Courier", 60, "normal"))
        self.goto(0, -60)
        self.color("blue")
        self.write(f"THE BLUE TEAM WINS", align="center", font=("Courier", 40, "normal"))

    def game_over(self):
        self.goto(0, 10)
        self.color("white")
        self.write(f"GAME OVER", align="center", font=("Courier", 60, "normal"))
        self.goto(0, -60)
        self.color("white")
        self.write(f"ITS A DRAW", align="center", font=("Courier", 40, "normal"))
