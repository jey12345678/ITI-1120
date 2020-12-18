#Lecture 13

l = [1,2,3,5,5,7,10,10]

def count(l,x):
    '''
    (list,x) -> int
    '''

    # n = len(l)

    counter = 0 #1

    for element in l: #n*1

        if element == x: #n
            counter = counter+1 #<= n

    return counter#1
        
    

def triplicates(l):

    n = len(l) #1

    for i in range(0,n): # 1*n

        for j in range(0,n)): # (n)^2

            for k in range(j+1,len(l)): #(n)^3

                if(l[i] == l[j] and l[j] == l[k] and i != k and i != j and j != k): #5*(n)^3
                    return True #<= 1

    return False #<=1

print(triplicates(l))

# 2 + n + n^2 + 6*n^3 = O(n+ n^2+ n^3) = O(n^3)

def triplicates_via_count(l):

    for item in l: # n
        if count(l,item) >= 3: #n^2 
            return True#<= 1

    return False #<= 1

# n^2 + n +1 = O(n + n^2) = O(n^2)

def k_same_count(l,k):
    '''
    (list,int) -> bool
    '''

    for item in l: 
        if count(l,item) >= k:
            return True

    return False

#0(n^2)

def triplicates_via_sort(l):
    sl = sorted(l) # 0 (n*log n)
    n = len(l)

    for i in range(n-2): #n-2
        sl[i] == sl[i+2]: # n-2
            return True#<= 1

    return False#<=1

# 1 + 2n -4 + n*log n = O(n+n*log n) = O(n*log n) So its a much better solution.

def k_same_via_sort(l,k):

    sl = sorted(l) # O(n*log n)

    for i in range(n - k+1): # n-2
        if sl[i] == sl[i+k-1]: # n-2
            return True #<= 1

    return False #<= 1


def aha(l,x):
    '''
    (list,number) ->None
    Precondiiton: List has at least one element
    '''

    l[0] = 999
    x = 888

num = 100
t = [1,1,1]
aha(t,num)
print(num)
print(t)

#Prints:
#100
#[999,1,1]
#Explanation
#Immutable
#int, float,bool,strings,tuples
#tuples are lists that cannot be changed.

#Mutable
#List


#Stack                          Heap

#num [100]

#t ----------Address----------> [1,1,1]



#l = t, references to the exact same list [1,1,1]
#x = num, 100 is stored in x.
#x [888]

#Everything in function disappears
#Prints num, which is 100 and then [999,1,1]








        



