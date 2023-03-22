import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()

for i in range(5):
    t.penup()
    t.goto(-i*10,-i*10)
    t.pendown()
    for f in range(4):
        t.forward(20*(i+1))
        t.left(90)

wn.mainloop()

