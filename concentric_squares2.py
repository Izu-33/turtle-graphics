import turtle as tt
from random import choice
import time


time.sleep(3)
num_squares = 20
length = 400
offset = 10
double_length = 20
animation_speed = 10
x, y = -200, -200

tt.speed(animation_speed)
tt.hideturtle()

fill_colors = ["red", "green", "blue", "hotpink"]

def squares(side, color):
    tt.fillcolor(color)
    tt.begin_fill()
    for _ in range(4):
        tt.forward(side)
        tt.left(90)
    tt.end_fill()

for count in range(num_squares):
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    color_index = count % len(fill_colors)
    color = fill_colors[color_index]
    squares(length, color)
    x = tt.xcor() + offset
    y = tt.ycor() + offset
    length = length - double_length

tt.exitonclick()