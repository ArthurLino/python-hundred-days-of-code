from turtle import Turtle
from random import randint


class Car(Turtle):

    def __init__(self, color, move_distance):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1.5)
        self.setheading(180)
        self.color(color)
        self.penup()
        self.goto(x=280, y=randint(-280, 280))
        self.move_distance = move_distance
        self.move()

    def move(self):
        self.fd(self.move_distance)
