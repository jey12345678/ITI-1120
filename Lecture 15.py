#Lecture 15

lst = [[3,5,7,9],[0,2,1,6],[3,8,3,1]]

print(lst[0])

print(lst[1])

print(lst[2])

print(lst[0][0])

print(lst[1][2])

print(lst[2][0])

m = []

for i in range(10):
    l = [1]*10 #creates a list with 10 ones
    m.append(l)

print(m)
print()

for item in m:
    for x in m:
        print(x, end = " ")

    print()

print("\n\n\n\n")
print("printing again \n")

def is_diagonal(m):
    '''
    (2D -list of int) -> bool
    '''
    #m is diagonal if all the elements not on the diagonal are 0

    #1. m is a square matrix and all of the elements on the diagonal are zero.

    for i in range(len(m)):
        #m[i] is a row
        if(len(m[i]) != len(m)):
            return False

    # m is a square matrix here
    #2. all the elements not on the diagonal are zero.
    for i in range(len(m)):
        #m[i] is a row.
        for j in range(len(m[i])):
            if(m[i][j] != 0 and i != j):
                return False

    return True

#listOfVotes = ["Biden","Biden","Trump","Biden","Kanye West","Jo","Trump","Biden"]

#Biden appears 75,000,000 votes and Trump 74,000,000 Jo: 2,000,000 and KW: 50,000

#[["Biden",75 000 000],[Trump,74 000 000]]

def frequency(a):
    '''
    (list of str) -> 2D list
    '''
    f= []

    for i in range(len(a)):
        #a[i] is a city.
        found = False
        for j in range(len(f)):
            if(a[i] == f[j][0]):
                found = True
                f[j][1] = f[j][1]+1

            if(found == False):
                f.append(a[i],1)
    return f

def num_distinct(l):
    len(frequency(l))

def is_unique(l):
    return len(frequency(l)) == len(l)


#main

cities = ["mostar","sarajevo","pairs","mostar","melbourne","budapest","melbourne","melbourne"]
print(frequency(cities))
#[["mostar",2],["sarajevo",1],["melbourne,3],[budapest,1]]

#O(n)
def print_ints(n):

    for i in range(1,n+1):
        print(i)

#O(n)
def print_odd_ints(n):

    for i in range(1,n,2):
        print(i)
        print("*")

#Creates all possible pairs of numbers with 5.
def print_something(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,j)

def mystery(n):
    print("n = ",n)
    #This line is executed log base 2 of n times.
    while n > 1:
        n = n//2
        print(n)
    

    print("n = ",n)




            

    
