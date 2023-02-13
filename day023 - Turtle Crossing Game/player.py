from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.setheading(90)
        self.move_distance = MOVE_DISTANCE

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.sety(self.ycor() + self.move_distance)

    def level_up(self):
        self.reset_position()
        self.level += 1
