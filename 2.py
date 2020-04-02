import turtle
colors=["red","orange", "yellow", "green", "blue", "purple"]
t=turtle.Pen()
turtle.bgcolor('black')
for x in range (259200):
    t.pencolor(colors[x%6])
    t.width(x/200+1)
    t.forward(x)
    t.left(120)
