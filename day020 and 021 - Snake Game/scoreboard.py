from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, screen_height):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=(screen_height/2) - 36)
        self.color("white")
        self.update(f"Your Score: {self.score}")

    def increase_score(self):
        self.score += 1
        self.update(f"Your Score: {self.score}")

    def update(self, writing):
        self.clear()
        self.write(writing, False, align="Center", font=('arial', 12, 'normal'))

    def game_over(self):
        self.update(f"Game Over. Final Score: {self.score}")