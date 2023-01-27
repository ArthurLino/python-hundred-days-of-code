import turtle as t
from random import choice
import colorgram

screen = t.Screen()
screen.colormode(255)

don = t.Turtle()
don.speed("fastest")
don.hideturtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(tuple(color.rgb))

NUMBER_OF_DOTS = 10 * 10
DOT_SIZE = 20
GAP_SIZE = 50

don.up()
don.setheading(-135)
don.forward(GAP_SIZE*5)
don.setheading(0)

x = don.position()[0]

for i in range(NUMBER_OF_DOTS):

    if i % 10 == 0 and i != 0:
        don.setx(x=x)
        y = don.position()[1]
        don.sety(y+GAP_SIZE)

    don.dot(DOT_SIZE, choice(rgb_colors))
    don.forward(GAP_SIZE)

screen.exitonclick()
