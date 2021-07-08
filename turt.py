from turtle import Turtle

class Turt(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5,1.5)
        self.left(90)
        self.penup()
        self.goto(0,-280)
    def up(self):
        newx=self.xcor()
        newy=self.ycor()
        self.goto(newx,newy+20)
    def down(self):
        newx = self.xcor()
        newy = self.ycor()
        self.goto(newx, newy - 20)
    def reverse(self):
        self.goto(0,-280)

