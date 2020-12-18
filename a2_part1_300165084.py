#ITI 1120
#Assignment 2 Part 1
#Jeyaparan,Jeyason
#300165084


import math
import random

def elementary_school_quiz(flag, n):
    '''
    (int,int) -> int

    Precondition: flag is 0 or 1, n is 1 or 2

    Returns the number of correct answers a student got for a randomly generated quiz.
    '''
    numQuestionsRight = 0
    randomNumOne = random.randint(0,9)
    randomNumTwo = random.randint(0,9)
    
    if( n == 1 and flag == 0):
        
        questionOneAnswer = int(input("Question 1: What is the result of "+str(randomNumOne)+" - "+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne-randomNumTwo
        if(questionOneAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight+1
            
    elif(n == 2 and flag == 0):

        questionOneAnswer = int(input("Question 1: What is the result of "+ str(randomNumOne)+"-"+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne - randomNumTwo

        if(questionOneAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight +1

        randomNumOne = random.randint(0,9)
        randomNumTwo = random.randint(0,9)
            
        questionTwoAnswer = int(input("Question 2: What is the result of "+ str(randomNumOne)+"-"+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne - randomNumTwo

        if(questionTwoAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight+1
    
    elif(n == 1 and flag == 1):

        questionOneAnswer = int(input("Question 1: What is the result of "+str(randomNumOne)+"^"+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne**randomNumTwo

        if(questionOneAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight+1
        
    elif(n == 2 and flag == 1):
        
        questionOneAnswer = int(input("Question 1: What is the result of "+str(randomNumOne)+"^"+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne**randomNumTwo

        if(questionOneAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight+1

        randomNumOne = random.randint(0,9)
        randomNumTwo = random.randint(0,9)
            
        questionTwoAnswer = int(input("Question 2: What is the result of "+ str(randomNumOne)+"^"+str(randomNumTwo)+"?"))

        actualAnswer = randomNumOne**randomNumTwo

        if(questionTwoAnswer == actualAnswer):
            numQuestionsRight = numQuestionsRight+1
    
    return numQuestionsRight

def high_school_quiz(a,b,c):
    '''
    (number,number,number) -> None

    Prints the quadratic equation and then solutions to the quadratic equation.
    '''

    if(a == 0 and b != 0 and c!= 0):
        x1 = -c/b
        print("The linear equation ",b,"x + ",c,"= 0 \nhas the following root/solution: ",x1)
        
    elif(a == 0 and b == 0 and c == 0):
        print("The quadratic equation ",a,"x^2 +",b,"x + ",c,"\nis satisifed for all numbers x.")
        
    elif(a == 0 and b == 0 and c != 0):
        print("The quadratic equation ",a,"x^2 +",b,"x + ",c,"\nis satisifed for no number x.")
        
    elif((b**2 -4*a*c) == 0):
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        print("The quadratic equation ",a,"x^2 + ",b,"x + ",c,"= 0 \nhas only one solution,a real root: ",x1)
    elif((b**2 - 4*a*c) <0):
        imaginaryVal = (math.sqrt(abs(b**2 - 4*a*c)))/(2*a)
        realPartOfNum = -b/(2*a)
        print("The quadratic equation ",a,"x^2 + ",b,"x + ",c,"= 0 \nhas the following two complex roots: \n", realPartOfNum,"+ i",imaginaryVal," \n and \n",realPartOfNum,"- i",imaginaryVal)

    else:
        x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        print("The quadratic equation ",a,"x^2 + ",b,"x + ",c,"= 0 \nhas the following two real roots: \n",x1,"and",x2)
    



# main

# your code for the welcome message goes here

print("*******************************************")
print("*                                         *")
print("*----Welcome to my math quiz-generator----*")
print("*                                         *")
print("*******************************************")

name= input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    answer = -1
    print("****************************************************************************")
    print("*                                                                          *")
    print("*    ",name,"welcome to my quiz-generator for elementary school students.  *")
    print("*                                                                          *")
    print("****************************************************************************")

    subOrExpAns = int(input(name+" what would you like to practice? Enter:\n0 for subtraction\n1 for exponentiation\n"))
    if(subOrExpAns != 0 and subOrExpAns != 1):
        print("Invalid chose. Only 0 or 1 is accepted.")
    else:
        numPracticeQuestions = int(input("How many practice questions would you like to do? Enter 0,1, or 2: "))

        if(numPracticeQuestions == 2):
            print(name,"here is your 2 questions:")
            answer = elementary_school_quiz(subOrExpAns,numPracticeQuestions)
        elif(numPracticeQuestions == 1):
            print(name,"here is your question: ")
            answer = elementary_school_quiz(subOrExpAns,numPracticeQuestions)
        elif(numPracticeQuestions == 0):
            print("Zero questions.OK.Good bye")
        else:
            print("Only 0,1 or 2 are valid choices for the number of questions.")
            
        if(answer == 0):
            print("I think you need some more practice ",name,".")
        elif(answer == 1 and numPracticeQuestions == 2):
            print("You did ok ",name,",but I know you can do better.")
        elif(answer == 2 or (answer == 1 and numPracticeQuestions == 1)):
            print("Congratulations ",name,"! You'll probably get an A tommorow.")
        
elif status=='2':

    # your code for welcome message
    print("****************************************************************************")
    print("*                                                                          *")
    print("*         Quadratic equation, ax^2+bx+c = 0, solver for ",name,"           *")
    print("*                                                                          *")
    print("****************************************************************************")
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here
        question = question.strip()
        question = question.lower()

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            a = float(input("Enter the number of coefficient a:"))
            b = float(input("Enter the number of coefficient b:"))
            c = float(input("Enter the number of coefficient c:"))
            high_school_quiz(a,b,c)
            
 
else:
    # your code goes here
    print(name,"you are not a target audience for this software.")

print("Good bye "+name+"!")
