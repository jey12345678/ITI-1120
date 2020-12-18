#Lecture 23

#Efficient Sorting Algorithms
#Selection Sort O(n^2)

import random

def merge_sort(L): #O(n log n)
    '''
    (list) -> list
    '''

    if len(L) <= 1:
        return L[:]

    middle = len(L)//2
    L1 = merge_sort(L[:middle])
    L2 = merge_sort(L[middle: ])

    return merge(L1,L2)

    

def merge(L1,L2): #O(n1+n2)
    '''
    (list,list) -> list
    Merge sorted lists L1 and L2 into a new line.
    >>> merge([1,3,4,6],[1,2,5,7])
    [1,1,2,3,4,5,6,7]
    '''

    newL = []
    i1 = 0
    i2 = 0

    while(i1 != len(L1) and i2 != len(L2)): 
        if(L1[i1] <= L2[i2]):
            newL.append(L1[i1])
            i1 = i1+1
        else:
            newL.append(L2[i2])
            i2 = i2+1

    newL.extend(L1[i1:])
    newL.extend(L2[i2: ])
    return newL

def qs(a):
    '''
    (list) -> list
    '''

    if (len(a) <= 1):
        return a[:]

    x = random.choice(a)

    lt = []
    eq = []
    gt = []

    for item in a: #O(n)

        if item < x:
            lt.append(item)
        elif item == x:
            eq.append(item)
        else:
            gt.append(item)

    return qs(lt) + eq + qs(gt)


#n + (n-1) +(n-2)...+3+2+1 = O(n^2)
#Expected nlog n


    
        

    
