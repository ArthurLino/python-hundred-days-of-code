from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=x_position, y=0)

    def up(self):
        if 240 >= self.ycor():
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() >= -240:
            self.sety(self.ycor() - 20)
