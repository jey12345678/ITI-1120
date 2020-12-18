import math

#Programming Excersizes Labs

#Repeater: Excersize 1

def repeater(s1,s2,n):
    string = s1+s2
    finishedString = "_"+(string*n)+"_"
    return finishedString

#Testing
s1 = "AAA"
s2 = "x"
n = 3
    
print(repeater(s1,s2,n))

#Roots: Excersize 2
#We made this assumption of b*2- 4*a*c to evaluate to a positive number because in order for there to be two roots, the value of the discriminant has to be positive.
def roots(a,b,c):
    x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    print("The quadratic equation with coefficients a = ",a," and b = ",b," and c = ",c,"\n has the following roots: x1 = ",x1," x2 = ",x2,".")

#Testing
a = 1
b = 2
c = 1
roots(a,b,c)

#Real Roots: Excersize 3
def real_roots(a,b,c):
    hasRealRoots = (b**2 - 4*a*c)>= 0
    return hasRealRoots

#Testing
a = 1
b = 1
c = 1
print(real_roots(a,b,c))
    

#reverse(x):Excersize 4
def reverse(x):
    tensDigit = x//10
    onesDigit = x%10
    
    newNumber = onesDigit*10+tensDigit

    return newNumber

#Testing
number = 17
print(reverse(number))
print(10/7)


    
    





    

    
