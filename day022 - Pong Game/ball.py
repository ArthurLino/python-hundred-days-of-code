from turtle import Turtle
from random import choice

HEADING_MULTIPLIERS = [1, -1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.05
        self.x_move = 10
        self.y_move = 10
        self.define_direction()
        self.move()

    def move(self):
        self.goto(x=(self.xcor() + self.x_move), y=(self.ycor() + self.y_move))

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x_l_paddle(self):
        self.x_move = (abs(self.x_move))
        self.increase_speed()

    def bounce_x_r_paddle(self):
        self.x_move = -(abs(self.x_move))
        self.increase_speed()

    def reset(self):
        self.define_direction()
        self.goto(0, 0)
        self.move_speed = 0.05

    def define_direction(self):
        self.x_move = 10 * choice(HEADING_MULTIPLIERS)
        self.y_move = 10 * choice(HEADING_MULTIPLIERS)

    def increase_speed(self):
        self.move_speed /= 1.1
