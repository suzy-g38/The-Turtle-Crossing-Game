from turtle import Turtle, Screen
import time
from player import Player
from car import Car
from scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("White")
screen.setup(height=600,width=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.moving_up,"Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.moving_cars()

    #Colliding with the upper wall
    if player.ycor() > 280:
        player.set_position()
        scoreboard.increase_level()
        car.speed_increment()

    #Colliding with cars
    for each_car in car.car_list:
        if each_car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()