from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.set_position()
        self.setheading(90)
        self.speed("fastest")

    def moving_up(self):
        self.forward(10)

    def set_position(self):
        self.goto(x=0, y=-280)



