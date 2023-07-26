from turtle import Turtle
align = "center"
font = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.goto(0, 300)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=align, font=font)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file1:
                file1.write(str(self.high_score))
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=align, font=font)

