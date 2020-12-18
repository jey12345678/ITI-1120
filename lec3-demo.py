#If you only want to return one value
#return(1)

#How to return more than one value.
#return(10,15)

#For assignment, No if statements, loops and lists

#Strings

#How to create a String

word = "LOL"
print(word)

s2 = "This is also a String"

#Use single quotes first and then double quote for quoting someone.
doubleQuote = 'A famous designer one said: " The best things in life are good" '
print(doubleQuote)

#Use double quotes first  and then single quotes for apostraphies.

# What if... you want to print She said : "Let's go play tennis."
s3 = "She said: \"Let's go play tennis.\""
print(s3)

#"This is line one
#\n used for new line.
lineOne = "This is line one \n This is line two \n This is line three"
print(lineOne)

# \': single quote character \":single double quote character \n: new line \t:tab
# \\: Is for actually printing a backslash.

#Tab button
print("A\tB")

tabword = "A\tB" 
#len() is the length of a sequence.
print(len(tabword))

#Length is 3

spaceCharacter = " "
#Has a length of 1.

zeroLength = ""
#No characters.

#Concatanating two pieces of text
s = "rock"
t = "climbing"
print("rock"+"climbing")
x = s+" "+t
print(x)

#Cannot do "The year is "+2020
#Could only concatanate strings.

#Multiplaction of strings.
multiplicationStrings = 4*"la"
print(multiplicationStrings)

#BUT YOU CANNOT DO 4.0*"la"

#Prints both 2 and 10
print(2,10)

#Prints a string as new line
print()

#Concatenates s and t together.
print(s+t)

#puts together rock and climbing with space between them.
print(s,t)
x = 10

#Print strings like this in assignment
print("The square of",x,"is",x**2)

#Ask user for data and obtain the data.
name = input("What is your name? ")

#Stores name in name variable.
print(name)

city = input("Where would you want to travel " + name+ "?")
print(city)

#The duration is NOT A NUMBER it returns a string
duration = input("How many days do you want to stay in "+city+"?")

duration = int(duration)
print(duration)

print(float("83.4"))

#Chops off the decimal of float number.
print(int(7.5))

print(float(2))



