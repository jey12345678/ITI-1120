import turtle 
s=turtle.Screen() 
t=turtle.Turtle()

#Draw the big circle
t.circle(100)

#Draw the smaller circle
t.penup()
t.goto(0,10)
t.pendown()
t.circle(90)

#Draw the smaller circle
t.penup()
t.goto(0,40)
t.pendown()
t.circle(60)

#Draw the smaller circle
t.penup()
t.goto(0,85)
t.pendown()
t.circle(10)

#Draw the horizontal line
t.penup()
t.goto(-150,95)
t.pendown()
t.forward(300)

#Draw the vertical line
t.penup()
t.goto(0,250)
t.setheading(270)
t.pendown()
t.forward(300)

#Draw the right diagonal line
t.penup()
t.goto(150,250)
t.right(45)
t.pendown()
t.forward(400)

#Draw the left diagonal line.
t.penup()
t.goto(-150,250)
t.left(90)
t.pendown()
t.forward(400)





