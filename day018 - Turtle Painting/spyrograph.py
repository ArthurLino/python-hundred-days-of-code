import turtle as t
from random import randint

screen = t.Screen()
screen.colormode(255)

don = t.Turtle()

don.speed("fastest")

for i in range(90 + 1):
    don.circle(100)
    don.setheading(i * 4)
    don.pencolor((randint(0, 255), randint(0, 255),randint(0, 255)))

screen.exitonclick()
