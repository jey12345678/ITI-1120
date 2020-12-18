#Lecture 19
import random

class Point:

    pi = 3.14
    

    def __init__(self,xcoord = 0,ycoord = 0):
        '''
        (Point,number,number) -> None
        >>>p = Point(2,3)
        >>>p.x
        >>>2
        >>>p.y
        >>>3
        initialize point coordinate to (xcoord,ycoord)
        '''

        self.x = xcoord
        self.y = ycoord

    def get(self):
        '''
        (Point) -> tuple
        '''

        return (self.x,self.y)

    def setx(self,xcoord):
        '''
        (Point,number) -> None
        '''
        self.x = xcoord

    def sety(self,ycoord):
        '''
        (Point,number) -> None
        '''

        self.y = ycoord

    def move(self,dx,dy):
        '''
        (Point,number,number) -> None
        change the x and y coordinates to dx and dy
        '''

        #Use class variables for constants, and you get their values using Point.variable.
        self.x = self.x+dx + Point.pi
        self.y = self.y+dy

    def __eq__(self,other):
        '''
        (Point,Point) -> bool
        '''
        return self.x == other.x and self.y == other.y

    #When you just want to see the value of Point.
    def __repr__(self):
        '''
        (Point) ->None
        '''

        return "Point("+str(self.x)+","+str(self.y)+")"

    #When you want to print Point.
    def __str__(self):
        '''
        (Point) -> None
        '''
        return "I am a point with the following coordinates: ("+str(self.x)+","+str(self.y)+")."
        

    #dir(Point) shows all the methods that is in Point class

#if pi is a global variable, there won't be any errors.
#pi = 3.14

x= 5
print(x)
l = [1,5,0]
print(l)

p = Point(2,3)
print(p)
#Prints what's stored in variable p, which is gibberish
#But you want it to print Point(2,3), which could do by using the __repr__ function.

#If you want to print something more user friendly, code that myself

#Creating a Card Game

#Create a class called Card
#If you give the Card object, a rank and a suit, card is made. Ex. c = Card("?","spades")
#Unicode characters for symbols on cards.
#Spades: \u2660
#Hearts: \u2661
#Diamond:\u2662
#Clover:\u2663
class Card:

    def __init__(self,rank,suit):
        '''
        (Card,str,str) -> None
        '''
        
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        '''
        (Card) -> str
        '''
        
        return self.rank
    
    def get_suit(self):
        '''
        (Card) -> str
        '''
        return self.suit

    def __repr__(self):
        '''
        (Card) -> str
        '''

        return "Card("+self.rank+","+self.suit+")"

    def __eq__(card1,card2):
        return card1.rank ==  card2.rank

#For a deck we don't need any info from the user, so constructor should look like this Deck(). d = Deck().
class Deck:

    suits = {"\u2660","\u2661","\u2662","\u2663"}
    ranks = {"2","3","4","5","6","7","8","9","10","J","Q","K","A"}

    def __init__(self):
        self.deck = []

        for rank in Deck.ranks:
            for suit in Deck.suits:
                #rank, suit, creates a card and adds it to my list.
                self.deck.append(Card(rank,suit))
                
    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()

    #Get length of deck using object orientated way.
    def len(self):
        return len(self.deck)

    #To call it using the classical way.
    def __len__(self):
        return len(self.deck)
    
    
    

    

    
        
        

    
        
        
            
                
                
        
    
        
    
    
    
