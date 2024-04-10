import turtle
import time


time.sleep(3)
num_circles = 25
radius = 20
offset = 10
animation_speed = 0

turtle.speed(animation_speed)
turtle.hideturtle()

for count in range(num_circles):
    turtle.circle(radius)
    x = turtle.xcor()
    y = turtle.ycor() - offset
    radius = radius + offset
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
