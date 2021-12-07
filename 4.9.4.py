import turtle
Sanyi = turtle.Turtle()
ablak = turtle.Screen()
ablak.bgcolor("Black")
turtle.pensize(4)
Sanyi.speed(1000)
Sanyi.pensize(3)
Sanyi.color("Red")

def spiral():
    for i in range(4):
        Sanyi.forward(150)
        Sanyi.right(90)

for i in range(20):
    spiral()
    Sanyi.left(18)
ablak.mainloop()