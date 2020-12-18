#Lecture 17
#set is a collection of unordered distinct elements or objects

s = {2,10,8}
print(s)
type(s)

s.add(1000)
print(s)

#Cannot do s[1] or s.sort() or slicing

#Can use in operator.

for item in s:
    print(item)

int("25")

int(4.54)

l = list(range(10))

str(3)


l.append(8)
l.append(5)
l.append(8)
l.append(8)

set(l)

list(set(l))

print(s)
s.add(2)

s.add("winter is coming")
print(s)

#unordered list
#append O(1)
#removing O(n)
#searching (in): O(n)

#sorted list
#add: O(n)
#removing: O(n)
#binary: O(log n)

#sets
#add: O(1)
#remove: O(1)
#searching(in): O(1)

#1 50 57 89 100 120 345
#In sorted list, you could access predesessor O(log n)
#sets: O(n)

wordList = open("/Users/share/dict/words").read().lower().split()
print("The number of words in the English dictionary is: ",len(wordList))

#O(n)
def palindrome(words):
    '''
    (list of str) -> list of str
    Returns a list of all palindromes in English
    '''

    pal = [] #1
    for w in words: # n*1
        if(w  == w[ : : -1]): #n
            pal.append(w) #n

    return pal #1

#O(n^2)
pal = palindrome(wordList)

#O(n)

def ananim(words):
    ana = [] #1
    ws = set(words)
    for w in words: #O(n)
        if w[: :-1] in ws: #O(n)
            ana.append(w) #O(n)

    return ana #O(1)

ana = ananims(wordlist)

d = {}

print(type(d))
s =set()

print(d)
d["APPL"] = "Apple Inc"
d["GOOG"] = "Google Inc"
print(d)

print("APPL" in d)
print("GOOG" in d)
print("YHOO" in d)

def frequency_dict(book):
    '''
    (list of str) -> dict
    '''

    freq = {}
    for word in book:
        if word in freq:
            freq[word] = freq[word]+1
        else:
            freq[word] = 1

    return freq
        

    


