from turtle import Turtle
FONT = ("FFF Forward", 20, "normal")
ALIGNMENT = "left"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-280, y=250)
        self.write(f"Level : {self.level}",align=ALIGNMENT,font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0,y=0)
        self.write("Game Over", font=FONT, align="center")
