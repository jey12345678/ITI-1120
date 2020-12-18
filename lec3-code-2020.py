import math

# this function computes area of a triangle given its base and height
# and it returns the area
def area_or_triangle(base, heigt):
       
	area=base*heigt/2
	return area

# this function computes area of a triangle given its base and height
# it prints the area, and returns nothing
def area_or_triangle_void(base, heigt):
        area=base*heigt/2
	print(area)
	
def area_of_circle(radius):
    area=radius**2*math.pi
    return area



        
