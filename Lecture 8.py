##############
#Lecture 8
##############

word = "apple"

for bla in word:
    print(bla)
    print("************")
    
print("good bye")

def print_vowels(phrase):
    '''
    (str) -> None

    prints vowels in a given phrase.
    '''

    for char in phrase:

        if char in "aeiouAEIOU":
            print(char)

    print("good bye")

#Put example runs in doc strings.

def count_vowels(phrase):
    '''
    (str) -> int

    Returns the number of vowels in the phrase.
    >>>count_vowels("August")
    3
    >>>count_vowels("grrr")
    0
    '''

    #Called accumulator variable
    counter = 0

    for x in phrase:

        if x in "aeiouAEIOU":
            counter = counter+1

            #Short cut for adding one, for adding 10 for example its just counter+=10
            counter+=1
            
    return counter

print_vowels("August")

def only_vowels(phrase):
    '''
    (str) -> str
    Returns a string containing all the vowels in the phrase.
    
    >>> only_vowels("August")
    "Auu"
    >>> only_vowels("grrrr")
    ""
    '''
    vowels = ""

    for ch in phrase:

        if ch in "AEIOUaeiou":
            vowels = vowels + ch

    return vowels

l = [2,10,-5.4]

for x in l:
    print(x)
    print("********")

#Iterates over the n numbers from 0 up to n-1.
#for i in range(10):

#Iterates over the n numbers starting from i, to n-1.
#for i in range(i,n):

#Iterates over the n numbers, i+c,i+2c,i+3c to n-1.
#for i in range(i,n,c):

def draw_square():
    print()
    print("******")
    print("*    *")
    print("*    *")
    print("******")
    print()

#goes from 0,1,2,3 ... 8,9
for i in range(10):
    draw_square()

print("good bye")


#prints 0 to 9.
for i in range(10):
    print(i)
    
print("Good bye!")

#Prints from 1 to 10.
for i in range(1,11):
    print(i)

print("Good bye!")

#prints all single digit even numbers.
for i in range(-8,10):
    if i%2 == 0:
        print(i)

print("good bye")

#Add third parameter to for loop to skip index by 2.
for i in range(-8,10,2):
    print(i)

print("good bye")

#Blast rocket into space.
for i in range(1,11):
    print(10-i+1)

print("BLAST OFF!")

#A different way to blast rocket to space.
for i in range(10,0,-1):
    print(i)

print("BLAST OFF!")



    


    
