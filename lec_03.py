import math

#Lec 3 demo

#Boolean operator "and"


print(True and True)
print(True and False)
print(True and False)
print(False and False)


#Boolean operator "or"
print(True or True)
print(True or False)
print(True or False)
print(False or False)

x = 30
#x <0 or x>100
print(x<0 or x>100)

#If i DON'T want the range to be between 0 and 100.
print(not(x>=0 and x<=100))

#How to make variables


#Power function
pow(2,3)

#Create your own area of triangle function

def area_of_triangle(base,height):
    #Body of the function
    area = base*height/2
    return area

def area_of_triangle2(base,height):
    area = base*height/2
    print(area)
    
print(area_of_triangle(10,10))

def area_of_circle(radius):
    area = math.pi*pow(radius,2)
    return area

x1 = area_of_triangle(10,1)
x2 = area_of_triangle2(10,1)

print (area_of_circle(2))

#Prints 5.0 because x1, actually has the value of 5.0
print(x1)

#Prints None because x2 doesn't actually have the value of the area.
print(x2)

dir(math)




