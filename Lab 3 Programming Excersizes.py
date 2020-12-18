#ITI 1120
#Lab 3 Programming Excersizes
#Jeyaparan,Jeyason
#300165084

import math

def pay(hourlyWage,hours):
    '''
    (number,int) -> number

    Precondition: hours>= 0, wage>= 0

    Return the employee's pay,( if the employee worked any hours beyond 40 but less than or equal to 60, should be paid at 1.5 times the regular hourly wage. Any hours beyond 60 should be paid at 2 times the regular hourly wage.
    '''

    if(hours <= 40):
        employeePay = hours*hourlyWage
    elif(hours > 40 and hours <= 60):
        extraHours = hours - 40
        extraWage = extraHours*hourlyWage*1.5
        employeePay = hourlyWage*40 +extraWage
    elif(hours > 60):
        extraHours = hours - 60
        extraExtraWage = extraHours*hourlyWage*2
        extraWage = 20*hourlyWage*1.5
        employeePay = hourlyWage*40+ extraExtraWage+extraWage
        
    return employeePay

def rps(playerOneChoice,playerTwoChoice):
    '''
    (str,str) -> int

    Preconditions: playerOneChoice must be R,P or S and playerTwoChoice must be R,P or S

    Return -1 if player 1 wins the game and return 1 if player two wins.
    '''

    if(('R' in playerOneChoice and 'P' in playerTwoChoice) or ('P' in playerOneChoice and 'S' in playerTwoChoice) or('S' in playerOneChoice and 'R' in playerTwoChoice)):
        return 1
    elif(('P' in playerOneChoice and 'R' in playerTwoChoice) or ('S' in playerOneChoice and 'P' in playerTwoChoice) or('R' in playerOneChoice and 'S' in playerTwoChoice)):
        return -1
    else:
        return 0


    
    
        
    
