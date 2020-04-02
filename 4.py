import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#F1F1F1")
turtle.bgcolor('black')
side=20
myPen.penup()
myPen.goto(0,0) #position cursor at the bootom right of the screen
myPen.pendown()

for i in range (1,101):
  myPen.forward(side)
  myPen.left(92)
  side=side+7


myPen.penup()
myPen.goto(500,500)

#Start Spiral
for i in range (1,101):
   for j in range (0,101):
       myPen.forward(side)
       myPen.left(90)
   myPen.left(20)
   side=side+403
for i in range (1,101):
   for j in range (0,101):
       myPen.forward(side)
       myPen.right(90)
   myPen.right(20)
   side=side-403
