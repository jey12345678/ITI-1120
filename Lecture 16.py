#Lecture 16

import random
l = random.sample(range(1,1000001),1000)

print(50 in l)
print(417796 in l)

##l.index(417796)

#Searching for values

#Linear search
#O(n)
#<= 2n +3 = O(n)

def linear_search(L,v):
    '''
    (list, object) -> int
    '''

    n = len(L) #1

    for i in range(n): #n*1
        if L(i) == v:#n*1
            return i #1

    return -1 #1

#O(n*log n)

#l = [1,100,"today",True]
#Not comparable items.
#100 < "today"
#You are going to get an error.

#<= 3+7*log_2*n
#O log n

def binary_search(L,v):
    '''
    (list,object) -> int
    Precondition: L is sorted from the smallest to the largest.
    Every pair of elements is comparable.
    '''

    b = 0 #1
    e = len(L) -1 #1

    while b <= e:
        mid = (b+e)//2 #2

        if( v < L[mid]): #1
            e = mid -1 #1
        elif(v > L[mid]): #1
            b = mid +1 #1
        else: #v == L
            return mid #<=1

    return -1#<= 1

#Given a list of L, positive in k
#return k largest elements from L

k = n*log n < n + n*log n = O(n*log n)
#Algorithm 1
#1.sort L #O(n*log n) 
#2.return last k elements(return L[-k: ]) #k

O(n*k)
#Algorithm 2
#repeat k times:
#find the max in L #O(n)
#Add that max to the list results #1
#delete that max from L #(n)
#return the list results #k

k*(2n+k)< k*(2n+n) = 3kn = 0(kn)



        
            
            








