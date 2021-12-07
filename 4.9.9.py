import turtle
ablak = turtle.Screen()
ablak.bgcolor("black")

toll = turtle.Turtle()
toll.speed(3)
toll.pensize(3)
toll.pencolor("red")

for i in range(5):
        toll.forward(100)
        toll.right(144)

ablak.mainloop()