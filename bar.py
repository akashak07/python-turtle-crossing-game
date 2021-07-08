from turtle import Turtle
import random
COLOR=["red","orange","yellow","green","blue","purple"]
SM=5
IN=10
class Bar:
    def __init__(self):
        self.barlist=[]

    def creatbar(self):
        check=random.randint(1,6)
        if check==1:
            myb=Turtle()
            myb.shape("square")
            myb.shapesize(1,2)
            myb.penup()
            myb.color(random.choice(COLOR))
            yval=random.randint(-240,240)
            myb.goto(300,yval)
            self.barlist.append(myb)
    def barmove(self):
        for b in self.barlist:
            b.backward(SM)



