#Lecture 21

#Recursion

#Recursion runs forever, until it crashes because there isn't a condition.
##def silly_printer(n):
##    '''
##    (n) -> None
##    '''
##    print(n)
##    silly_printer(n-1)

def countdown(n):
    if n<= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n-1)

#main
#silly_printer(4)
countdown(4)

#Runs forever, because it only calls a function once, whereas in recursion it calls multiple functions.
def silly_printer_i(n):
    while True:
        print(n)
        n = n-1

#silly_printer_i(4)

def fact(n):

    if(n == 0):
        return 1
    else:
        res = n*fact(n-1)
        return res

print(fact(3))

##def summer(l):
##    if(len(l) == 0):
##        return 0
##    elif (len(l) == 1):
##        return l[0]
##    else:
##        return l[0] + summer(l[1: ])

def summer(l):
    if(len(l) == 0):
        return 0
    elif(len(l) == 1):
        return l[0]
    else:
        return summer(l[:len(l)//2]) + summer(l[len(l)//2 : ])
    
    


    


