from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=1.75, outline=None)
        self.up()
