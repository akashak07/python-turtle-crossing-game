from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.barspeed=0.10
        self.score=0
        self.color("black")
        self.penup()
        self.goto(-280,270)
        self.upscore()
    def upscore(self):
        self.write(f"Your level:{self.score}", align="left", font=("Courier", 10, "normal"))
    def hit(self):
        self.score+=1
        self.barspeed *=0.9
        print(self.barspeed)
        self.clear()
        self.write(f"Your level:{self.score}", align="left", font=("Courier", 10, "normal"))
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!", align="center", font=("Courier", 25, "normal"))

