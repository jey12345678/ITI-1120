#Lecture 14
#Trivia Quiz Creation

#0: question
#1-4: 4 possible answers
#5 Category
#6 difficulty

import random

def ask_question(q,p):
    print()
    print(q[0])

    for i in range(1,5):
        print(i,q[p[i-1]])

def raw_read_answer():
    try:
        ans = int(input("Answer (1,2,3, or 4): "))
        results = 10/ans
        return ans
    except ValueError:
        print("Error.Answer must be an integer.")
##    except ZeroDivisionError:
##        print("Division with zero error.")

    
    
def read_answer():
    ans = raw_read_answer()
    while ans not in [1,2,3,4]:
        print("Answer must be a 1,2,3,4")
        ans = raw_read_answer()

    return ans    
    
    

lines = open("quiz.csv").read().splitlines()

lives = 3
score = 0

questions = []
for line in lines:
    questions.append(line.split("\t"))

while lives >= 1:
    
    
    p = [1,2,3,4]
    random.shuffle(p)
    q = random.choice(questions)
    ask_question(q,p)
    ans = read_answer()

    if(p[ans-1]== 1):
        print("Correct")
        score = score + int(q[-1])
    else:
        print("Incorrect. The correct answer is:",q[1])
        lives = lives -1

    print("You have",lives,"lives left. Your score is: ",score)
    
    



    

    


