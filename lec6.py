def abs(x):
     if x<0:
          return -x
     else:
          return x

def abs_v2(x):
     if x<0:
          return -x
     return x

def abs_v3(x):
     if x<0:
          x=-x
     return x

def format_age(age):
     '''
     (int)->str
     Preconditions: age non-negative
     Returns a string representing somebody's age'''
     if age < 20:
          retval= str(age)
     elif age<30:
          retval ="twenty something"
     elif age<40:
          retval= "thirty something"
     else:
          retval="ancient"
     return retval



def letter_grade(grade):
     '''
     (int)->str
     Returns a string representing somebody's age'''
     
     if (grade>=80 and grade <=100):
          return 'A'
     elif (grade>=70 and grade <=79):
          return 'B'
     elif (grade >=60 and grade <=69):
          return 'C'
     elif (grade >=0 and grade<=59):
          return 'F'
     else:
          return "grade is not valid"


























































          
