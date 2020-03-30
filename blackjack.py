# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 10:45:23 2020

@author: willem
"""
import random

class Card:
    def __init__(self,suit,face,value):
        self.suit = suit
        self.face = face
        self.value = value
    
    def show(self):
        return("{} of {}".format(self.face,self.suit))
        


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for s in ['Spades','Clubs','Diamonds','Hearts']:
            for i in range(2,15):
                if i == 11:
                    f = 'Jack'
                    v = 10
                elif i == 12:
                    f = 'Queen'
                    v = 10
                elif i == 13:
                    f =  'King'
                    v = 10
                elif i == 14:
                    f = 'Ace'
                    v = 11
                else: 
                    f = i
                    v = i
                self.cards.append(Card(s,f,v))
                
    def show(self):
        for c in self.cards:
            c.show()
            
    def drawCard(self):
        return self.cards.pop()
    
            
class Player:
    def __init__(self,name, wallet):
        self.name = name
        self.hand = []
        self.tableCards =[]
        self.betMoney = 0
        self.wallet = wallet

    
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self
    
    
    
    def showCard(self):
        card = self.hand.pop()
        self.tableCards.append(card)
        # self.handValue += card.value
        card.show()
        print(self.name + " has " +card.show())      

    def calcValue(self):
        self.handValue = 0
        for card in self.tableCards:
            self.handValue += card.value                        
        return self.handValue
                
    def checkAces(self):
        foundace = False
        for i in range(len(self.tableCards)):
            if self.tableCards[i].face =='Ace':
                self.tableCards[i].value = 1
                self.tableCards[i].face='Ace2'
                foundace = True

                break
        return foundace
            
    def placeBet(self):
        
        while True:
            try:
                self.betMoney = int(input('How much would you like to bet? You have ${}  '.format(self.wallet)))
            except:
                print('That is not a valid amount')
                continue
            else:
                if self.betMoney > self.wallet:
                    print('You do not have that amount')
                    continue
                else:
                    print('Placed a bet of ${}'.format(self.betMoney))
                    self.wallet -= self.betMoney
                    break
                           
    def newGame(self):
        self.hand = []
        self.tableCards = []
        
            
            
  
            
def startgame():    
    deck = Deck()
    random.shuffle(deck.cards)
    bank = Player('Bank',2000)
    player = Player(input('What is your name?  '),500)
    return deck, bank, player

def restart():
    clear()
    bank.newGame()
    player.newGame()
    
def newRound():
    player.newGame()
    bank.newGame()
    player.placeBet()
    bank.draw(deck)
    bank.draw(deck)
    player.draw(deck)
    player.draw(deck)
    print(' ')
    bank.showCard()
    print(' ')
    player.showCard()
    player.showCard()
    player.calcValue()

def hitOrStand(challenger): 
    while True: 
        choice = str(input('Hit or Stand? ').lower())
        if 'hit' in choice:
            challenger.draw(deck)
            challenger.showCard()
            challenger.calcValue()


            if challenger.calcValue() <21:
                print("{} has a hand value of {}".format(str(challenger.name),challenger.handValue))
                print(' ')
                continue
            elif challenger.calcValue() >21 and challenger.checkAces()==False:
                print("{} has a hand value of {}".format(str(challenger.name),challenger.handValue))
                print(' ')
                break
            elif challenger.calcValue()==21:
                print("{} has a hand value of {}".format(str(challenger.name),challenger.handValue))
                print(' ')
                break
        elif 'stand' in choice:
            break
        else:
            print(' please choose hit or stand')
            continue
    

def bankTurn(defendant,challenger): 
        if challenger.handValue > 21:
            winner = defendant
            loser = challenger
            defendant.calcValue()

        
        elif challenger.handValue == 21:
            winner = challenger
            loser = defendant
            defendant.calcValue()

        else:
            defendant.showCard()
            defendant.calcValue()
            while True:
                if defendant.handValue >= challenger.handValue and defendant.handValue <= 21:
                    winner = defendant
                    loser = challenger
                    break
                elif defendant.handValue <= 17:
                    defendant.draw(deck)
                    defendant.showCard()
                    defendant.calcValue()
                    continue
                else:
                    winner = challenger
                    loser = defendant
                    break
        print("{} has a hand value of {}".format(str(defendant.name),str(defendant.handValue)))

        gameover(winner,loser)
            
            
def gameover(winner,loser):
    winner.wallet += (2*winner.betMoney)
    print(str(winner.name)+" has won the round and earned ${}".format(str(winner.betMoney+loser.betMoney)))
    winner.betMoney =0
    loser.betMoney =0
  
def playgame():
    playing = True
    while playing:
        newRound()
        hitOrStand(player)
        bankTurn(bank,player)
        playing = str(input('Play another round? (Y/N)').lower())=='y'

deck, bank, player = startgame()

playgame()

