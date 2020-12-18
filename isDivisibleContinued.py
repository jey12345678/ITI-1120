def is_divisible(n,m):
    '''
    (int,int) -> bool

    Returns true if n is divisible by m and false is n is not divisible by m.
    '''
    if(n%m == 0):
        return True
    else:
        return False

def is_divisible23n8(integer):
    '''
    (int) -> str

    Returns "yes" if the given number is divisible by 2 or 3 but not 8. Otherwise returns no.
    '''

    divisibleByThree = is_divisible(integer,3)
    divisibleByTwo = is_divisible(integer,2)
    divisibleByEight = is_divisible(integer,8)

    if((divisibleByTwo or divisibleByThree) and not(divisibleByEight)):
        return "yes"
    else:
        return "no"

integer = int(input("Enter an integer: "))
answer = is_divisible23n8(integer)
if(answer == "no"):
    print("It is not true that",integer,"is divisible by 2 or 3 but not 8.")
    
elif(answer == "yes"):
    print(integer,"is divisible by 2 or 3 but not 8.")


