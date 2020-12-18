#ITI 1120
#Assignment 2 Part 2
#Jeyaparan,Jeyason
#300165084

def min_enclosing_rectangle(radius,x,y):
    '''
    (number,number,number) -> (number,number)

    Return the x and y coordinates of bottom left corner of the smallest axis aligned rectangle that contains the circle with that radius.
    '''

    if(radius < 0):
        return None
    else:
        xRect = x - radius
        yRect = y - radius

        return (xRect,yRect)
    
def vote_percentage(results):
    '''
    str -> number

    Preconditions: The results has at least one yes or no and the only words present in results is yes,no and/or abstained.

    Returns the percentage of yes among all yes and no

    '''
    numOfYes = results.count("yes")
    numOfNo = results.count("no")

    totalNumOfYesNo = numOfYes+numOfNo

    votePercentage = numOfYes / totalNumOfYesNo

    return votePercentage

def vote():
    '''
    None -> None

    Prints the outcome of the vote, and determines whether the proposal passes or whether it fails.
    '''

    voteResult = input("Enter the yes,no, abstained votes one by one and then press enter: \n")

    votePercent = vote_percentage(voteResult)

    if(votePercent == 1.0):
        print("The proposal passes unanimously.")

    elif(votePercent >= (2/3) and votePercent < 1.0):
        print("The proposal passes with super majority.")
        
    elif(votePercent >= (1/2) and votePercent < (2/3)):
        print("The proposal passes with simple majority.")
        
    else:
        print("The proposal fails.")
    

    

    

    
