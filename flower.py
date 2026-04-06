import turtle
import random
screen = turtle.Screen()
screen.bgcolor("white")
f = turtle.Turtle()
f.speed(100000)
p = int(input("Введіть кількість пелюстків: "))
c = ["red"]
for _ in range(p):
    f.color(random.choice(c))
    f.begin_fill()
    for _ in range(2):
        f.circle(100, 60)
        f.left(120)
    f.end_fill()
    f.left(360 / p)
f.penup()
f.goto(0, -23)
f.color("yellow")
f.begin_fill()
f.circle(20)
f.end_fill()

f.goto(0, -25)
f.setheading(-90)
f.pendown()
f.color("green")
f.pensize(10)
f.forward(300)

f.hideturtle()
screen.mainloop()
