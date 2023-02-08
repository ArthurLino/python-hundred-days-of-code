from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(300-36)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setx(-100)
        self.write(self.l_score, align="left", font=("arial", 24, "normal"))
        self.setx(100)
        self.write(self.r_score, align="right", font=("arial", 24, "normal"))

    def increase_right_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_left_score(self):
        self.l_score += 1
        self.update_scoreboard()
