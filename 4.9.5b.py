import turtle
Sanyi = turtle.Turtle()
ablak = turtle.Screen()
ablak.bgcolor("black")
Sanyi.speed(1000)
Sanyi.color("red")

a = 0

def spiral():
    for i in range(1):
        Sanyi.forward(a)
        Sanyi.right(89)

for i in range(100):
    spiral()
    a = a + 1