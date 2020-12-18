import math
import turtle

#ITI 1120
#Assignment 1
#Jeyaparan,Jeyason
#300165084

######################
#Question 1
#######################
def f_to_k(t):
    '''
    (number) -> number

    Returns the temperature given in Fahrenheit, in degrees Kelvin.
    '''
    
    temperatureInKelvins = (5/9)*(t-32)+273.15
    return temperatureInKelvins

######################
#Question 2
#######################
def poem_generator():
    '''
    (None) -> None

    Prints a poem that includes the name and city of birth given by the user.
    '''
    
    name = input("Enter your name: ");
    city = input("Enter your city of birth: ")

    print("When",name,"stood with fiddle drawn\nWatching",city,"burn\nFlaunting his lack of concern\nAs ashes flew hither and yon!")

#########################
#Question 3
##########################
def impl2loz(w):
    '''
    (number) -> (int,float)

    Preconditions: w >= 0

    Returns a pair of numbers(l,0) and l is an integer and o is a non-negative number smaller than 16.
    '''

    l = int(w)
    
    o = 16*(w-l)

    return (l,o)

#####################
#Question 4
#####################
def pale(n):
    '''
    (int) -> bool

    Preconditions: n>= 1000 and n<= 9999,(in other words, n has to have 4 digits)

    Returns True if n is a pale number and returns false if n is not a  pale number.

    '''

    thousandsDigit = n //1000
    hundredsNumber = n %1000
    hundredsDigit = hundredsNumber//100
    tensNumber = hundredsNumber%100
    tensDigit = tensNumber//10
    onesDigit = tensNumber%10

    divisibleByFourChecker = onesDigit %4 == 0
    consecutiveThreeChecker = (thousandsDigit == 3 and hundredsDigit == 3) or (hundredsDigit == 3 and tensDigit == 3) or (tensDigit == 3 and onesDigit == 3)

    paleChecker = not(divisibleByFourChecker or consecutiveThreeChecker)

    return paleChecker

#####################
#Question 5
#####################
def bibformat(author,title,city,publisher,year):

    '''
    (str,str,str,str,int) -> str

    Returns a string with info given by the user in a special bibformat.
    '''

    formattedString = author+"("+str(year)+")."+title+"."+city+":"+publisher+"."
    return formattedString
#####################
#Question 6
####################
def bibformat_display():
    '''
    (None) -> None

    Prints a string in a special bibformat with user's info.

    '''

    title = input("Enter the title of a book: ")
    author = input("Enter the name of the author? ")
    year = int(input("What year was the book published?"))
    publisher = input("Enter the name of the publisher:")
    city = input("In what city are the headquarters of the publisher?")

    formattedString = bibformat(author,title,city,publisher,year)

    print(formattedString)
    
#######################
#Question 7
#######################
def compound(x,y,z):
    '''
    (int,int,int) -> bool

    Returns true if x is the only even number among the 3 integers and if at least one pair of three integers adds up to a number greater than 100.

    '''

    xChecker = (x%2 == 0) and (y%2 != 0) and (z%2 != 0)
    addsToHundredChecker = ((x+y) > 100) or ((y+z) > 100) or ((z+x) > 100)

    compoundChecker = xChecker and addsToHundredChecker

    return compoundChecker

#######################
#Question 8
#######################

def funct(p):
    '''
    (number) -> None

    Preconditions: p >= 11

    Prints the solution for r in an equation: (5^(r^2))-p+10 = 0
    '''
    
    r = math.sqrt(math.log((p-10),5))
    print("The solution is r: ",r)

#######################
#Question 9
#######################
def gol(n):
    '''
    (number) -> int

    Preconditions: n>=1

    Returns the minimum number of times that n needs to be divided by 2 in order to get a number equal to or smaller than 1.
    '''
    
    minimumNumber = math.ceil((math.log(n,2)))
    return minimumNumber

#######################
#Question 10
#######################
def draw_rocket():
    '''
    (None) -> None

    Draws a rocket.
    '''

    s=turtle.Screen() 
    t=turtle.Turtle()
    t.pensize(11)


    #Draw 3 Circles

    t.penup()
    t.goto(0,130)
    t.pendown()
    t.circle(40)

    t.penup()
    t.goto(0,-10)
    t.pendown()
    t.circle(50)

    t.penup()
    t.goto(0,-130)
    t.pendown()
    t.circle(50)

    #Draw the curve
    t.left(81)

    t.penup()

    t.goto(-100,100)
    t.pendown()

    #Draw the first left curve at the top.
    for x in range(42):
        t.forward(5)
        t.right(1)

    t.penup()
    t.goto(100,100)
    t.pendown()
    t.left(-80)
    t.right(220)

    #Draw the first right curve at the top.
    for x in range(42):
        t.forward(5)
        t.left(1)

    t.left(380)
    t.penup()
    t.goto(100,100)
    t.pendown()

    #Draw the cross curve betweeen left and right curve.
    for x in range(41):
        t.forward(5)
        t.left(1)

    

    t.penup()
    t.goto(100,100)
    t.pendown()   
    t.left(-380)

    t.right(-290)
    
    #Draw the bottom right curve.
    for x in range(59):
        t.forward(-5)
        t.right(1)

    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.right(290)
    t.left(305)

    #Draw the bottom left curve.
    for x in range(59):
        t.forward(-5)
        t.left(1)
        
    t.penup()
    t.goto(-68,-183)
    t.left(-305)
    t.left(180)
    t.pendown()
    
    #Draw the straight line at the bottom.
    t.forward(135)

    
    #Draw the left wing.
    t.penup()
    t.goto(-119,-50)
    t.pendown()
    t.left(250)
    t.forward(190)
    t.right(580)
    t.forward(124)

    
    #Draw the right wing.
    t.penup()
    t.goto(118,-50)
    t.pendown()
    t.right(460)
    t.forward(190)
    t.left(580)
    t.forward(128)

    t.penup()
    
    #Move the turtle away from the rocket.
    t.goto(-500,0)
    
#######################
#Question 11
#######################
def cad_cashier(price,payment):
    '''
    (number,number) -> number

    Preconditions: payment >= price, price >= 0

    Returns the change in Canadian dollars, which is based on rounding to the closest five cents.
    '''

    change = payment - price
    change = round((change*100)/5)*5/100

    return change;

#######################
#Question 12
#######################
def min_CAD_coins(price,payment):
    '''
    (number,number) -> (int,int,int,int,int)

    Preconditions: payment >= price, price> = 0

    Returns five numbers that represent the minimum number of coins owed to the customer.
    '''
    

    change = cad_cashier(price,payment)

    numOfCentsLeft = round(change*100)

    t = numOfCentsLeft // 200
    numOfCentsLeft = numOfCentsLeft - (t*200)
    l = numOfCentsLeft // 100
    numOfCentsLeft = numOfCentsLeft - (l*100)
    q = numOfCentsLeft // 25
    numOfCentsLeft = numOfCentsLeft - (q*25)
    d = numOfCentsLeft //10
    numOfCentsLeft = numOfCentsLeft - (d*10)
    n = numOfCentsLeft //5
    numOfCentsLeft = numOfCentsLeft - (n*5)

    return(t,l,q,d,n)

    
             

    

