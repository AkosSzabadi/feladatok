import turtle
ablak = turtle.Screen()
toll = turtle.Turtle()
toll.pensize(3)
ablak.bgcolor("Lightblue")


def negyzetek(n):
        for i in range(4):
            toll.forward(n)
            toll.left(90)

n = 20
x = 0
y = 0

for  i in range(5):
    negyzetek(n)
    n += 20
    x += - 10
    y += - 10
    toll.penup()
    toll.goto(x, y)
    toll.pendown()

ablak.mainloop()