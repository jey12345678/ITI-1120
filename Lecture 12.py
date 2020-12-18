#Lecture 12

#Do all the problems in Chapter 5
#Not the Big O notation


def maximum(l):
    '''
    (list) -> number

    Precondition: l is a non empty list of numbers.

    Given a list of numbers l, the function should return the namxium number of the list.
    '''

    #n = len(l)

    current_Max = l[0] # 1

    for item in l: #1. number of elements in the list. 1*n
        if item > current_max: # 1*n
            current_max = item # <= 1*n

    return current_max #1

# <= 3n+2 = O(n)

#<=4n -1000 = O(n)

#Which one is better

#What really matters is the n value.

#<= 3n+2 = O(n)

def maximum_v2(l):
    l.sort() #O(n * log n)
    return l[-1] #1

#O(n*log n), it is worse because it uses n*log n.

def maximum_v3(l):
    return max(l)

#Loosely related to assignment
def positional_min(x,y):

    #x = [1,2.5,100,-8]
    #y = [2,0,80,20]
    result = True #1

    for i in range(len(x)): #1*n
        if(x[i] > y[i]): #1*n
            result = False #<= #1*n

    return result #1

#3n+2 = O(n)

def duplicates(l):
    '''
    (list) -> bool
    '''

    for i in range(0,len(l)): #1*n

        for j in range(0,len(l)):  #1*n^2

            if(l[i] == l[j] and i!= j): #2*n^2 because two comparisons
                return True #1

    return False #1

# 3*n^2 + n + 1 = O(n^2)

#O(n*log n)

def duplicates_v2(l):
    '''
    (list) -> bool

    '''
    l.sort() # n*log n

    for i in range(0,len(l)-1): #1*(n-1)
        if l[i] == l[i+1}: #1*(n-1)
            return True #1

    return False #1

# n*log n + n-1 +n -1 + 1 = n*log n + 2n -1 = O(n*log n)

#O(n*1) fastest
#O(n *log n) #second fastest
#O(n *n) # slowest

            



