import turtle
s=turtle.Screen()
t=turtle.Turtle(shape='turtle')



# your code should go right after this line


#Draw a circle for the sun
t.penup()
t.goto(-100,100)
t.pendown()
t.circle(50)

#Draw the 1st wave.
t.penup()
t.goto(-300,0)
t.pendown()
t.setheading(-45)
t.circle(50,90)


#Draw the second wave.
t.setheading(-45)
t.circle(50,90)

#Draw the third wave.
t.setheading(-45)
t.circle(50,90)

#Draw the fourth wave.
t.setheading(-45)
t.circle(50,90)

#Draw the fifth wave.
t.setheading(-45)
t.circle(50,90)

#Draw the sixth wave
t.setheading(-45)
t.circle(50,90)

#Move the turtle to the bottom of the waves.
t.penup()
t.goto(-10,-70)
t.pendown()




