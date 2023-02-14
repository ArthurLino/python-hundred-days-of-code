from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        with open("high-score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=(screen_height/2) - 36)
        self.color("white")
        self.update()

    def increase_score(self):
        self.score += 1

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", False, align="Center", font=('arial', 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update()
        self.save_high_score()

    def save_high_score(self):
        with open("high-score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
