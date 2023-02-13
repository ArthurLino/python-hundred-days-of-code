import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

new_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(new_player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    if new_player.ycor() >= screen.window_height() / 2:
        new_player.level_up()
        car_manager.increase_difficult()
        scoreboard.increase_score()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(new_player) < 20:
            game_is_on = False

screen.exitonclick()
