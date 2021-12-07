import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")

def square(l):
    for i in range(4):
        turtle.forward(l)
        turtle.left(90)

for i in 'Red', 'Blue' , 'Yellow' , 'Green':
    turtle.pencolor(i)
    square(20)
    turtle.penup()
    turtle.forward(40)
    turtle.pendown()

