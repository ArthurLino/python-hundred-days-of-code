import time

from ball import Ball
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

l_paddle = Paddle(x_position=-350)
r_paddle = Paddle(x_position=350)

screen.update()

screen.onkey(l_paddle.down, "s")
screen.onkey(l_paddle.up, "w")
screen.onkey(r_paddle.down, "Down")
screen.onkey(r_paddle.up, "Up")

ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor() > 300 - 50 or ball.ycor() < -300 + 20:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l_paddle()

    if ball.xcor() >= 370:
        scoreboard.increase_left_score()
        ball.reset()

    if ball.xcor() <= -370:
        scoreboard.increase_right_score()
        ball.reset()

    time.sleep(ball.move_speed)

screen.exitonclick()
