#Lecture 22

#>= O(2^n)
def power_set(l):
    '''
    (list) -> 2D list

    Returns all the possible subsets of l
    '''

    if len(l) == 0:
        return [[]  ]

    pps = power_set(l[1:])

    fps = pps[:] #copy all the subsets without l[0]

    for item in pps:
        fps.append([l[0]] + item)

    return fps

#Is P == NP?

def mypow(x,n):
    '''
    (number,int) -> number
    Preconditions: n is non-negative integer
    Precondition: x is non-negative 
    x = 0 and n = 0 excluded
    '''

    if n == 0:
        return 1
    
    else:
        return x*mypow(x,n-1)
    
def mypow(x,n):
    '''
    (number,int) -> number
    Preconditions: n is non-negative integer
    Precondition: x is non-negative 
    x = 0 and n = 0 excluded
    '''

    if n == 0:
        return 1
    
    else:
        #Crashes because n never reaches 0, and recursion calls exceed above 1000.
        #return mypow(x,n/2)*mypow(x,n/2)

        
        #return mypow(x,n//2)*mypow(x,n//2) #it is only true when n is even.

        res = mypow(x,n//2)

        if n%2 == 0:
            return res*res
        else:
            return x*res*res

#O(n)    
def mypow_i(x,n):
    p =1 #1

    for i in range(n): #n
        p = p*x #n

    return p #1


    
    
    
    
    
    
    

