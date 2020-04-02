import turtle
colors=["red","purple", "blue", "green", "orange", "yellow"]
turtle.bgcolor('black')
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#F1F1F1")

side=400
myPen.penup()
myPen.goto(-200,-200) #position cursor at the bootom right of the screen
myPen.pendown()

#Start Spiral
for i in range (1,100):
     myPen.forward(side)
     myPen.left(90)
     side=side-4
for j in range (1,200):
     myPen.forward(side)
     myPen.right(90)
     side=side+4
for i in range (1,10):
     myPen.color("#000000")
     myPen.forward(side)
     myPen.left(90)
     side=side-4
