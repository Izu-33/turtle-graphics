import turtle
import time


time.sleep(3)
turtle.speed(0)
val = 5
offset = 5

for x in range(100):
    val += offset
    turtle.forward(val)
    turtle.right(90)

turtle.exitonclick()