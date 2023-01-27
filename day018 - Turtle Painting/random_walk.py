import turtle as t
from random import randint

screen = t.Screen()
screen.colormode(255)

don = t.Turtle()

don.pensize(10)
don.speed(10)

for i in range(500):
    don.forward(50)
    don.setheading(90 * randint(0, 3))
    don.pencolor((randint(0, 255), randint(0, 255),randint(0, 255)))

screen.exitonclick()
