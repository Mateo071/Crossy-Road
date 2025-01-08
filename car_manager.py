from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        dice_roll = randint(1, 6)
        if dice_roll == 5:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=1.75, outline=None)
            new_car.color(choice(COLORS))
            new_car.setheading(180)
            new_car.up()
            new_car.goto(315, randint(-240, 240))
            self.all_cars.append(new_car)

    def drive_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def delete_car(self):
        del self