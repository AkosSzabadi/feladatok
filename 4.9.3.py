import turtle
ablak = turtle.Screen()
ablak.bgcolor("lightblue")
toll = turtle.Turtle()
toll.pensize(3)

def negyzetek(hosszusag, szog, oldalak):
        for i in range(oldalak):
            toll.forward(hosszusag)
            toll.left(szog)

for i in range(2):
    negyzetek(100,45,4)

ablak.mainloop()