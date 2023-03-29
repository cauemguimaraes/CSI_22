import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.color("blue")

t.penup()
t.goto(-200, 0)
t.pendown()

for i in range(100):
    t.forward(i*1.5)
    t.right(90)


t.penup()
t.goto(200, 0)
t.pendown()

for i in range(100):
    t.forward(i*1.5)
    t.right(89)


wn.mainloop()
