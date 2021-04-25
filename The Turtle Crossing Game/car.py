from turtle import Turtle
import random
COLORS = ["yellow","blue","green","red","orange","violet"]
STARTING_MOVING_DISTANCE = 5
SPEED_INCREMENT =10

class Car:

    def __init__(self):
        self.car_list = []
        self.new_coord = random.randint(20,50)
        self.car_speed = STARTING_MOVING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(x=300,y=random.randint(-250,250))
            car.setheading(180)
            car.speed("fastest")
            self.car_list.append(car)

    def moving_cars(self):
        for car in self.car_list:
            car.forward(STARTING_MOVING_DISTANCE)

    def speed_increment(self):
        self.car_speed += SPEED_INCREMENT




