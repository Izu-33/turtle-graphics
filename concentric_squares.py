import turtle as tt
from random import choice
import time


time.sleep(3)
num_squares = 20
length = 20
offset = 10
double_length = 20
animation_speed = 10

tt.speed(animation_speed)
tt.hideturtle()

fill_colors = ["red", "green", "blue", "hotpink"]

def squares(side):
    color = choice(fill_colors)
    tt.fillcolor(color)
    tt.begin_fill()
    for _ in range(4):
        tt.forward(side)
        tt.left(90)
    tt.end_fill()

for count in range(num_squares):
    squares(length)
    x = tt.xcor() - offset
    y = tt.ycor() - offset
    length = length + double_length
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

tt.exitonclick()