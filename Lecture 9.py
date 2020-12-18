#####
#Lecture 8
########

def print_chars(s):
    for ch in s:
        print(ch)

def print_chars_V2(s):
    for i in range(len(s)): #I want i to be 0, then 1,then 2, etc.
        print(s[i])

def print_every_second(s):
    for i in range(0,len(s),2): # I want i to be 0,2,4,6
        print(s[i])
    

s = "today"

#given string = "abcdef"
#result: "ba*dc@fe*"
#Put a star if the pair has a vowel.
#@ sign otherwise.
#Given "abcdefg" , result is ba*dc@fe*g
#Given: "a"
#Result: "a"

def flip_consecutive_disjoint_pairs_anddd(string):
    '''
    (str) -> str

    >>>flip_consecutive_disjoint_pairs_anddd("abcdef")
    "ba*dc@fe*"
    >>>filp_consecutive_disjoint_pairs_anddd("abcdefg")
    ba*dc@fe*g
    >>>filp_consecutive_disjoint_pairs_anddd("a")
    "a"

    '''

    stringLength = len(string)

    if len(string)<= 1:
        return string
    
    newStr = ""
    for i in range(0,len(string)-1,2): #"abcdef"   0,1,2,3
        pair = string[i+1]+string[i]
        newStr = newStr+pair
        if has_vowel(pair) == True:

            newStr = newStr+ "*"
        else:
            newStr = newStr+"@"

    if(len(s) %2 != 0):
        newStr = newStr+ string[len(string)-1]

    return newStr

def has_vowel(string):
    
    if("a" in string or "e" in string or "i" in string or "o" in string or "u" in string):
        return True
    else:
        return False


#Use slicing

def flip_consecutive_disjoint_pairs_anddd(string):
    '''
    (str) -> str

    >>>flip_consecutive_disjoint_pairs_anddd("abcdef")
    "ba*dc@fe*"
    >>>filp_consecutive_disjoint_pairs_anddd("abcdefg")
    ba*dc@fe*g
    >>>filp_consecutive_disjoint_pairs_anddd("a")
    "a"

    '''

    stringLength = len(string)

    if len(string)<= 1:
        return string
    
    newStr = ""
    for i in range(0,len(string)-1,2): #"abcdef"   0,1,2,3
        pair = string[i : i+2] # s[0:2]
        
        newStr = newStr+pair[ : :-1] #Reverses the string.
        if has_vowel(pair) == True:

            newStr = newStr+ "*"
        else:
            newStr = newStr+"@"

    if(len(string) %2 != 0):
        newStr = newStr+ string[len(string)-1]

    return newStr   

def flip_k_consecutive_disjoint_anddd(string,k):
    '''
    (str,int -> str
    >>>flip_k_consecutive_disjoint_anddd("abcdfr",3)
    cda*rfd@
    >>>flip_k_consecutive_disjoint_anddd("abcdfr",4)
    dcba*fr
    '''


    if len(string)<= 1:
        return string
    
    newStr = ""
    for i in range(0,len(string)-1,k): #"abcdef"   0,1,2,3
        block = string[i : i+k] # s[0:2]
        
        newStr = newStr+block[ : :-1] #Reverses the string.
        if has_vowel(block) == True:

            newStr = newStr+ "*"
        else:
            newStr = newStr+"@"

    newStr = newStr + string[len(string)-len(string)%k : ]

    return newStr  
 


        
        
    


