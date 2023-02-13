from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.sety(260)
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.setx(-280)
        self.write(f"Game is over. Final Score: {self.score}", align="left", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.setx(-280)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
