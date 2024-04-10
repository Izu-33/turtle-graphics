import turtle


turtle.bgcolor('black')
turtle.speed(0)
colors = ['white', 'orange', 'red',
          'yellow', 'green', 'blue', 'cyan']

for i in range(120):
    turtle.pencolor(colors[i%6])
    turtle.circle(190-i/2, 90)
    turtle.left(90)
    turtle.circle(190-i/3, 90)
    turtle.left(60)

