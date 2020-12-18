#Lecture 18

#In the past we created integers, and created objects of type int, and used float objects, and string objects
#and lists, and tuples, sets and dictionaries, boolean types.


#In trivia game, all the elements were stored in 2D Lists.

#Easier to just create our own data type.
#g[i][0]
#g[i][1]
#q.question
#q.A1
#q.A2
#q.A3
#q.A4
#g.diff
#g.category

#How do we design our own data types?

#Represent plane using x coordinates and y coordinates

#P[i][0] gives you the x coordinates of the plane.
#P[i][1] gives you the y coordinates of the plane.


#The right hand side creates an object of type Turtle.
#The address of that object gets stored in the variable alex.

import turtle

alex = turtle.Turtle()

#What attributes does such object have?
#color, shape, speed
#What could you do with it? methods



#Always captialize the first letter of an class
class Point:
    
    #When calling Point(2,3) does the following steps.
    #1.Object of type Point gets created.
    #2.Address of that object is produced.
    #3.If there is an __init__ function, it runs it.
    #by passing this address of the object created into self.
    #Self is the object that you are just about to create.
    def __init__(self,xcoord = 0,ycoord = 0,col = "black"):
        '''
        (Point,float,float,str) -> None
        '''
        
        self.x = xcoord
        self.y = ycoord
        self.col = col

    def move(self,dx,dy):
        '''
        (Point,float,float) -> None
        '''
        
        self.x = self.x+dx
        self.y = self.y+dy

    def __eq__(p1,p2):
        '''
        (Point,Point) -> bool
        '''

        return p1.x == p2.x and p1.y == p2.y

        
    




#main
p = Point(2,3,"red")
q = Point(3.51,4,"black")

#You could change the x coordinates and y coordinates later.
##p.x = 4
##p.y = 8

#Could use this format as well: Point.move(p,100,200)

#You could create an integer object using its constructor, but that's just bad syntax.
x = int(10)
print(x)

#If you put nothing in the brackets, then 0 is printed.
x = int()
print(x)



#Same thing applies for string.

#Used to seeing this.
s = "snow"
print(s)

#But you could create a string like this.
s = str("today")
print(s)

#Default string.
s = str()
print(s)

#Default list.
l = list()
print(l)

#Default float.
f = float()
print(f)

q = Point()
print(q.x)
print(q.y)

r = Point(7.11)
print(r.x)
print(r.y)

#Difference between class and object, is class is just a recipe, but then an object is living.

#Objects behave like lists, sets and dictionaries and are mutable.
    

#To make an object you need to call a function with the name of the class and then you give it pieces of data.
       
s1 = "today"
s2 = "today"
print(s1 == s2)
l1 = [1,2,3]
l2 = [1,2,3]

print(l1 == l2)

print(l1 is l2)

##p = Point(2,3)
##q = Point(2,3)
##print(p == q)
#Point.__eq__(p,q)

#Prints false because they aren't located in the same place in the memory.






    

