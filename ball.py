from turtle import Turtle
import random
global i
global j
arr = [-1.5, -1.25, -1.1, -1, 1, 1.1, 1.25, 1.5]
i = random.choice(arr)
j = random.choice(arr)
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DarkSlateGrey")
        self.penup()
    def direction(self):
        i = random.choice(arr)
        j = random.choice(arr)
    def move(self):

        new_x = self.xcor() + i*3
        new_y = self.ycor() + j*3
        self.goto(new_x, new_y)