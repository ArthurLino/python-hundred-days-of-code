import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
from turtle import Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Arthur Lino | Snake Game")
screen.tracer(0)

scoreboard = Scoreboard(screen_height=SCREEN_HEIGHT)
food = Food()
snake = Snake()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    if snake.head.distance(food) <= 1:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.ycor() < -(SCREEN_HEIGHT//2-10) or snake.head.ycor() > SCREEN_HEIGHT//2-10 or \
            snake.head.xcor() < -(SCREEN_WIDTH//2-10) or snake.head.xcor() > SCREEN_WIDTH//2-10:
        scoreboard.reset()
        snake.reset()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
