import turtle

t = turtle.Turtle()
s = turtle.Screen()

t.speed("fastest")


def clear():
    t.clear()


def move_forward():
    t.fd(10)


def move_backward():
    t.bk(10)


def rotate_positive():
    t.left(+10)


def rotate_negative():
    t.right(+10)


s.listen()
s.onkeypress(key="w", fun=move_forward)
s.onkeypress(key="s", fun=move_backward)
s.onkeypress(key="d", fun=rotate_negative)
s.onkeypress(key="a", fun=rotate_positive)
s.onkey(key="c", fun=clear)
s.exitonclick()
