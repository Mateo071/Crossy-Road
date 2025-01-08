from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.color('green')
        self.up()
        self.goto_start()

    def move_forward(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
        
    def move_back(self):
        self.setheading(270)
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
        
    def move_right(self):
        self.setheading(0)
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def goto_start(self):
        self.goto(STARTING_POSITION)