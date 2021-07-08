from turtle import Turtle,Screen
from turt import Turt
from bar import Bar
import time
from scoreboard import Score
from finishline import Finish
sc=Screen()
sc.setup(600,600)
sc.bgcolor("white")
sc.tracer(0)

bar=Bar()

turtle=Turt()

score=Score()

finish=Finish()

sc.listen()
sc.onkey(turtle.up,"Up")
sc.onkey(turtle.down,"Down")
gameon=True
while gameon:
    time.sleep(score.barspeed)
    sc.update()
    bar.creatbar()
    bar.barmove()
    for b in bar.barlist:
        if b.distance(turtle)<32:
            gameon=False
            score.game_over()
        if turtle.ycor() > 250:
            score.hit()
            turtle.reverse()



sc.exitonclick()