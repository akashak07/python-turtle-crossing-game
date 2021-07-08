from turtle import Turtle
class Finish(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("black")
        self.penup()
        self.goto(0,270)
        self.write("Finish Line!!", align="center", font=("Courier", 10, "normal"))
        self.goto(300,260)
        while self.xcor()>-300:
            self.pendown()
            self.width(5)
            self.backward(50)
            self.penup()
            self.backward(10)

