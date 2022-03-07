import turtle as t

import ball
from SCORBOARD import Scoreboard
Screen = t.Screen()
Screen.setup(800, 600)
Screen.bgcolor("azure")
Screen.listen()

lpaddle = t.Turtle("square")
lpaddle.penup()
lpaddle.color("DarkSlateGrey")
lpaddle.shapesize(1, 8)
lpaddle.goto(-350, 0)
lpaddle.left(90)

rpaddle = t.Turtle("square")
rpaddle.penup()
rpaddle.shapesize(1, 8)
rpaddle.color("DarkSlateGrey")
rpaddle.goto(350, 0)
rpaddle.left(90)
striker = ball.Ball()
striker.speed("fastest")

scoreboard = Scoreboard()
def up():
    lpaddle.fd(10)


def down():
    lpaddle.backward(10)


def up1():
    rpaddle.fd(10)


def down1():
    rpaddle.backward(10)


def game_over():
    Screen.exitonclick()
game_is_on = True
total_game = True


while game_is_on:

    striker.move()
    Screen.onkeypress(up, "W")
    Screen.onkeypress(down, "S")
    Screen.onkeypress(up1, "U")
    Screen.onkeypress(down1, "J")

    if striker.ycor() < 300 and striker.ycor() > 290:
        ball.j *= -1

    if striker.ycor() > -300 and striker.ycor() < -290:
        ball.j *= -1

    if striker.xcor() < -340 and striker.xcor() > -350:
        if striker.ycor() < lpaddle.ycor() + 80 and striker.ycor() > lpaddle.ycor() - 80:
            ball.i *= -1

    if striker.xcor() > 340 and striker.xcor() < 350:
        if striker.ycor() < rpaddle.ycor() + 80 and striker.ycor() > rpaddle.ycor() - 80:
            ball.i *= -1
    if striker.xcor() > 390:
        game_is_on = False
        scoreboard.increase_score_left()
    if striker.xcor() < -390:
        game_is_on = False
        scoreboard.increase_score_right()

    if game_is_on == False:
        striker.goto(0, 0)
        striker.direction()
        striker.move()
        game_is_on = True
