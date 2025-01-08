import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, 'w')
screen.onkey(player.move_forward, 'Up')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'd')
screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_back, 's')
screen.onkey(player.move_back, 'Down')

def level_up():
    player.goto_start()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() >= 300:
        level_up()

screen.exitonclick()