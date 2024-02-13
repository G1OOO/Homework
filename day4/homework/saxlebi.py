from turtle import *

# Set the width of the pen
width(3)

# Set background color to baby blue
bgcolor("lightblue")

# Draw the first house and yard
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

# Move to draw the second house
penup()
goto(200, 0)
pendown()

# Draw the second house and yard
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

# Move to draw the third house
penup()
goto(-200, -200)
pendown()

# Draw the third house and yard
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

# Draw the sun
penup()
goto(-200, 200)
pendown()
color("yellow")
begin_fill()
circle(50)
end_fill()

# Draw the stars
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

# Hide the turtle
hideturtle()

# Keep the window open
mainloop()
