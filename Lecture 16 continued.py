#Lecture 16 continued

def swap_first_two(a):
    tmp = a[0]
    a[0] = a[1]
    a[1] = tmp

def swap_first_two_continued(a):
    a = [a[1],a[0]]

l = [100,1]
print(l)
swap_first_two(l)
print(l)

l = [100,1]
swap_first_two_continued(l)
print(l)



def swap(x,y):
    tmp = x
    x = y
    y = tmp
    

##a =100
##b = 1
##print(a,b)
##swap(a,b)
##print(a,b)

#Prints the same thing, so it doesn't work and this is because it doesn't return the x and y values.


#Don't do a ==b
#a = b

#Instead do:
##tmp = a
##a =b
##b = tmp
##print(a,b)


#Learn how to sort.
#Selection Sort



#O(n^2)
def selection_sort():
    '''
    (list) -> None
    '''

    #repeat the procedure
    for i in range(0,len(L)-1):
        #find minimum in sublist l starting with i and go to the end.
        min_index = i
        for j in range(i+1,len(L)):
            if(L[j] < L[min_index]):
                min_index = j
                
        #swap L[i] and min if needed.
        temp = L[i]
        L[i] =min_current
        L[min_index] = temp

    
#for i in range(n):
#        for i in range(i+1,n):
#           print("*")
# <= n+ (n-1) +(n-2) +(n-3)
#(n+1) + (n+2) +(n+3)

#n*(n+1)/2
#n^2/2 + n/2
# O(n^2)




            

    
    



