#Lecture 11
import random

#While loops

##if CONDITION:
##    statement(s)

##while CONDITION:
##    statement(s)

for i in range(10,0,-1):
    print(i)

print("blastoff")

i = 10

##while CONDITION:
##    print(i)

#infinite while loop
while i>0:
    print(i)
    i = i -1
print("blastoff")

##while True:
##    print(i)


answer = input("Yes or No do you want to buy this ticket?")

#This is because you enter yes, yes equals to Yes,so that part is false, but yes doesn't equal to no so that is true, so if you use or
#you will enter the loop anyways, but if you use and, you won't enter the loop.
while (answer.lower() != "yes" and answer.lower()!= "no"):
    print("Incorrect input. Please answer yes or no.")
    answer = input("Yes or No do you want to buy this ticket?")

#If it is either yes or no you want to enter the loop, then use or operator.
#CANNOT USE BREAK. 

print("Next step is ...")

answer = input("Yes or No do you want to buy this ticket?")

##while True:
##    if answer == "yes":
##        break
##    if answer == "no":
##        break

#Questions
#Are we going to be marked based on efficiency now, or are we just being marked on whether or not it works?
#Just out of curiousity, do you think we are able to complete assignment 4 with the knowledge we have now, or should be wait until other lessons are taught by you?
#Do we need to look out for preconditions because lets say if the user enters a wrong value, are we supposed to check for that or not?
def print_until_vowel(s):
    '''
    (str) -> None
    
    '''
    i = 0
    while i< len(s) and s[i] not in "aeiouAEIOU":
        print(s[i],end = "")
        i = i+1

    print("\nGood bye")

#n (positive integer)
#even n/2
#odd 3*n +1

##n = 12
##12, 6, 3, 10 .... (eventually get down to) 1

def colltaz(n):

    #We don't know if the while loop is infinite or not.

    while n != 1:
        if( n%2 == 0):
            n = n//2
        else:
            n = 3*n +1


    return True

for i in range(1,1000001):
    colltaz(i)

print("The conjecture is true for the first million numbers")

def guessing_game():

    print("I'm think of a number in the set 1,2,3, ......,1000")

    tries = 10

    x = random.randint(1,1000) #[1,2,3,,,,,,1000]

    guess = int(input("Try and guess"))

    tries = tries -1

    while guess != x and tries >0:

        if guess < x:
            print("Wrong! Too low")

        elif guess > x:
            print("Wrong! Too high.")
        else:
            print("You win. Great work!")

        guess = int(input("Try and guess"))
        tries = tries -1

    if guess == x:
        print("You win!!! Great work")
    else:
        print("You are not a very good guesser. Go read up on binary search.")
        

guessing_game()
    
    
    
    

    
    
    
    

    


    



