import turtle as t

don = t.Turtle()

INTERNAL_ANGLES_SUM = 360
POLYGON_SIDE_SIZE = 100

for polygon_number_of_sizes in range(3, 11):
    for _ in range(polygon_number_of_sizes):
        don.forward(POLYGON_SIDE_SIZE)
        don.left(INTERNAL_ANGLES_SUM / polygon_number_of_sizes)


screen = t.Screen()
screen.exitonclick()
