#Lecture 20

#Finishing Objects


class Animal:

    def __init__(self,species = "Animal",language = "make sounds"):
        self.spec = species
        self.lang = language

    def print_info(self):
        print(self.spec,self.lang)

    def __repr__(self):

        return "Animal(\""+self.spec+"\",\""+self.lang+"\")"

    def __str__(self):

        return "I am a "+self.spec+" and I "+self.lang+"."
    
    def speak(self):
        print("I am a ",self.spec," and I", self.lang)
    

class Gottem:
    def speak(self):
        print("bla")
    

class Bird(Animal):
    '''
    Called extending
    '''
    
    def __init__(self,species = "Animal",beak_length = 0,language = "make sounds"):
        self.beak_length = beak_length
        super().__init__(species,language)

    '''
    overriding
    '''

    def speak(self):
        print(3*self.lang)

    def report_beak_length(self):
        return self.beak_length

    def print_info(self):
        print(self.beak_length)
        super().print_info()


class myStr(str):
    def first_last_same(self):
        if self[0] == self[-1]:
            return True
        else:
            return False
        

def f(b):
    a = 6
    return a*b

a = 0

#What does this print?
print(f(3))
print("a is ",a)

    
    
    
        
    

    
    
class Point:
    pass

