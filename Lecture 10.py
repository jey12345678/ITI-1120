#Lists

s= "lajksdlkj"
s = "today"

listOfNumbers = [2,-1,100]
print(listOfNumbers)

#Tells you how many elements list has.
len(listOfNumbers)

#Use [] for getting item of list.
itemOne= listOfNumbers[0]
itemTwo = listOfNumbers[1]
itemThree = listOfNumbers[2]

#You could use slicing

newList = listOfNumbers[len(listOfNumbers)-1]

l = [2,-1,100,4,1,100,3,45]

print(l[0:3])
#Prints out [-2,-1,100]

print(l[: 3])
#Prints out [-2,-1,100]

print(l[3:7])
#Prints out [4,1,100,3]

print(l[ : :2])
#Prints out [2,100,1,3]

print(l[ : :-1])
#Prints out [45,3,100,1,4,100,-1,2]

print(l)
#Prints out [2,-1,100,4,1,100,3,45]

print(-1 in l)
#Prints out True

print(101 in l)
#Prints out False

#You could compare lists
listOne = [2,10,0]
listTwo = [2,10,0]

#These two lists are not the same objects because although they have the same content, they are stored in different locations in memory.

print(listOne == listTwo)
#Prints out True

s1 = "today"

print(s1[0])
#Prints out t

#You cannot do s[0] = "T" because strings are unmutable, so you cannot change them.
#Int, floats and bool are also unmutable

#Lists are mutable so you can change them.

l[0] = 100000000000000

print(l)

#Any data type could be mixed and be part of the list.
l[2] = "aja"

#Returns the length of the list.
print(len(l))

#Add items to the list and remove items to the list, dynamic.
l = [10,3,5]

#If it says function_descripter, in help() function, you just call it how you  would usually call a function.
#If it says method descripter, you have to use dot operator.

#To add elements to the end of the list.
l.append(10.13)
l.append(73)

#You could only add elements one at a time.
#But you could add a list to another list.
l.append([190,3])


#Prints: [10,3,5,10.3,73,[190,3]]
l.append(73)


len(l)
#Prints 6
#l[0] and l[1] are basically variable names.

print(l[5][0])
#Gets me to first element of the list in the list.

print(l[5][1])
#Gets me to the second element of the list in the list.

l.count(73)
#Prints 2 because there are two 

l.count(190)
#Prints 0 because 190 is in the list of the list, and not its own element.

l.count([190,3])
#Prints 1 because that exists in the list.

#190 in l
#Prints False because it doesn't exist by itself in the list.

#[190,3] in l
#Prints True because [190,3] is in the list.
l.remove(73)
l.remove(10.13)
#Removes 10.13

#l.remove(100)
#Error because 100 isn't in the list.

l.pop()
#Removes and returns the last element of the list.
#Removes and returns 73 in this case.

l.pop(1)
#Removes and returns the element in index 1.
#Removes and returns 3.

print(l)

l.pop()
l.append(-20)
print(l)

#To sum the elements of the list you use sum function
print(sum(l))
print(sum([1,3,10]))

#Lots of builtin methods used for lists.
print(type([2,34]))

#string s
r = ["today","is","a","nice","day"]
len(r)
#Prints out 5.

#Sometimes its a good idea to convert a string into a list.
q = list(s)

q[0] = "T"

#Use sort method to sort the list.
q.sort()
print(q)

q[0] = "t"
print(q)
q.sort()
print(q)

l = [10,-3,60,7]

help(list.sort)

l = [10,-3,60,7]

l.sort()
print(l)

l = [10,-3,60,7]
##q = l.sort() #the function returns None, so q is type none, so don't do this!!!!
##print(q[0])
#Iterable means anything you could loop over.

l = [8,-33,100,5]
#sorted() returns new sorted list.
q = sorted(l)
print(q)

#Using for loops with lists.
for item in l:
    print(item,end = " ")

print()

for i in range(len(l)):
    print(l[i],end = " ")

print()

#Find maximum of the list.

currentMax = l[0]

for item in l:
    
    if item > currentMax:
        currentMax = item

print("The maximum of",l,"is",currentMax)

#Find the minimum of the list.

currentMin = l[0]

for item in l:

    if item < currentMin:
        currentMin = item

print("The minimum of",l,"is",currentMin)

print(sum(l))

print()
currentSum = 0
for item in l:
    currentSum = currentSum + item

print("The sum of these elements",l,"is",currentSum)

print()

current_prod = 1
for item in l:
    current_prod = current_prod*item
print("The prod of these elements ",l,"is",current_prod)

#For 2+10, 2 is stored in memory and 10 is stored in memory and then two numbers are retrieved and CPU performs operation and the the 12 gets stored in memory.
# a = 100 000
#b = 100 000

# = is assignment operator, creates an integer 100 000 and then it goes to memory and finds a free location and stores 100 000. What gets stored in variables are the addresses not the objects.
#Once the object is created the address is stored in a variable, "a".
#What is actually stored in a is an address of the object.

# b stores a different address which holds 100 000.

#c, is a+b and it follows a, and finds the address there and follows it and retrieves an object which is 100 000.
#b, finds the address there and follows it to the location of 100 000 and retrieves it.
#Puts numbers in CPU register, and now CPU could perform operation.

#c now refers to the address of object 200 000.
#a == b, its true because the content at both of the locations are the same.
#But a is b, returns false because they don't have the same address.

def add(x):
    x = x+1

y = 100
add(y)

x = y

a = 100 000
b = 100 000
# a== b
#True
#a is b
#False
a = 100 000
b = 100 000
c =a
#c refers to the same location  as a

a = 55

#The variable x holds the address to [2,100]
x = [2,100]

#The variable y holds the address to [2,100] in a different location of the memory.
y = [2,100]

#The address of x is stored in z, so they take you to the same list.
z=x

#Change x[0] to 55, which will change z[0] to 55.
x[0] = 55
print(x)












