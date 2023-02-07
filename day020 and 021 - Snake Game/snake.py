from turtle import Turtle

SNAKE_STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        self.head.color("green")

    def create_snake(self):
        for pos in SNAKE_STARTING_POSITIONS:
            self.add_body_segment(pos)

    def add_body_segment(self, position):
        snake_segment = Turtle(shape="square")
        snake_segment.penup()
        snake_segment.color("lime green")
        snake_segment.goto(position)
        self.body.append(snake_segment)

    def extend(self):
        self.add_body_segment(self.body[-1].position())

    def move(self):
        for segment_index in range(len(self.body) - 1, 0, -1):
            next_x = self.body[segment_index - 1].xcor()
            next_y = self.body[segment_index - 1].ycor()
            self.body[segment_index].goto(next_x, next_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

