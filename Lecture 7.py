##########
#Lecture 7
##########

#x in s checks a substring of s, returns true or false
#x not in s checks if x is not a substring of s.
#s +t concatenation of s and t.
#s*n, n*s concatenation of n copies of s.
#s[i] character at index i of s.
#len(s) is the function length of string s.

s = "It's September"

print("ep" in s)
#Returns True

print("ep" not in s)
#Returns False

print("Sep" in s)
#Returns True

print("sep" in s)
#Returns False

print(" " in s)
#Returns True

print(' ' in s)
#Returns True

print("apple" < "fig")

#Returns true because f comes after a in the alphabet, and think of it like a dictionary or in a phone book.
print("atu" < "actru")
#Returns False, because t comes after c, compare first letters, and then second letters and so on.

print("atu" < "atuk")
#Returns True because lower string comes first.

print("sept" == "sept")
#Returns True

print("sept" == "Sept")
#Returns False

print("1" <"2")
#Returns True

print("2"<"12")
#Returns False, because 2 is ahead of 1, in 12.

print("b" <"a")
#Returns False as b comes after a.

print("B" <"a")
#Returns True because Captail letters comes before lower case letters.

print("?" < "!")
#Returns False because the ! mark comes before the question mark.

#To check order of characters, use function:
ord("?")
#Returns 63
ord("!")
#Returns 33

#Because 63 isn't lower than 33, false is returned.

#Use unicode characters to print more characters.

#Regular character
print("a")

#Use unicode character,has four digits
#Prints a spade
print("\u2660")

#String is a sequence of characters, and there is an order to the characters.
print(s[0])
print(s[1])
print(s[2])

print(s[len(s)-1])

#If you use negative number, python starts at the back.
print(s[-1])
print(s[-2])

#To go from the back to get to the start of the string you could use s[-len(s)], not s[len(s)-1] because from the back it starts at -1, and not 0.
print(s[-len(s)])

#From start index to end index-1.
print(s[5:8])
print(s[0:3])

#From beginning up to but not including 3.
print(s[ : 3])

#From 3 all the way to the end.
print(s[3: ])

#Start from x, go up to position y, and skip 2.
print(s[ : :2])

#prints string backwards.
print(s[ : :-1])

print(s[ : len(s)//2: ])

#For string variables.
s = "today"

#Strings are unchangable, or immutable below code causes an error.
##s[0] = "T"

s = "today"

#New string gets created here.
s = "tommorow"

s = "today"

#For loops

for ch in s:
    print(ch)
    print("*****")

print("good bye")

def print_vowels(phrase):
    '''
    (str) -> None

    Prints the vowels in the given phrase.
    '''

    #Option 1

##    for ch in phrase:
##        if "a" == ch or "e" == ch or "i" == ch or "o" == ch or "u" == ch:
##            print(ch)

    #Option 2
    for ch in phrase:
        if ch in "aeiouAEIOU":
            print(ch)

    print("good bye")

    #Turn phrase to lower case as third option.
    
    



      
