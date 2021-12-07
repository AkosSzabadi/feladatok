import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")


toll = turtle.Turtle()
toll.pencolor("red")
toll.pensize(3)


for i in range(3):
    toll.forward(100)
    toll.left(120)
    toll.forward(100)

ablak.mainloop()