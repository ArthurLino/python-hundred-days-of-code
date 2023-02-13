from random import choice
from car import Car
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.colors = COLORS
        self.move_increment = MOVE_INCREMENT
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        if randint(1, 3) == 1:
            self.cars.append(Car(choice(self.colors), self.move_distance))

    def move_cars(self):
        for car in self.cars:
            car.move()

    def increase_difficult(self):
        self.move_distance += self.move_increment
        for car in self.cars:
            car.move_distance = self.move_distance
