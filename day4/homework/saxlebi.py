from turtle import *

width(3)

bgcolor("lightblue")

color("red")
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

right(90)
color("yellow")
begin_fill()
right(135)
forward(70)
right(90)
forward(70)
right(135)
forward(100)
end_fill()

penup()
goto(200, 0)
pendown()

color("red")
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

right(90)
color("yellow")
begin_fill()
right(135)
forward(70)
right(90)
forward(70)
right(135)
forward(100)
end_fill()

penup()
goto(-200, -200)
pendown()

color("red")
begin_fill()
for _ in range(4):
    forward(100)
    left(90)
end_fill()

right(90)
color("yellow")
begin_fill()
right(135)
forward(70)
right(90)
forward(70)
right(135)
forward(100)
end_fill()

penup()
goto(-200, 200)
pendown()
color("yellow")
begin_fill()
circle(50)
end_fill()

penup()
goto(200, 150)
pendown()
color("white")
for _ in range(5):
    forward(50)
    right(144)

penup()
goto(-100, 100)
pendown()
for _ in range(5):
    forward(30)
    right(144)

penup()
goto(100, 50)
pendown()
for _ in range(5):
    forward(40)
    right(144)

hideturtle()

mainloop()
