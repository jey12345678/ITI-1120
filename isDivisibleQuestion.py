
def is_divisible(n,m):
    '''
    (int,int) -> bool

    Returns true if n is divisible by m and false is n is not divisible by m.
    '''
    if(n%m == 0):
        return True
    else:
        return False

n = int(input("Enter 1st integer: "))
m = int(input("Enter 2nd integer: "))

answer = is_divisible(n,m)
if(answer == True):
    print(n,"is divisible by",m)
else:
    print(n,"is not divisible by",m)






    
