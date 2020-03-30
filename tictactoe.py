# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def startgame():
    positions = list(map(str,range(1,10)))
    p1marker,p2marker = firstplayerpick()
    player1input(positions, p1marker,p2marker)

def firstplayerpick():
    p1XorO = input("Please pick a marker 'X' or 'O' ").upper()
    if p1XorO not in ('X','O'):
        startgame()
    else:
         p1marker = p1XorO
         if p1marker == 'X':
             p2marker = 'O'
             return p1marker,p2marker
         else:
             p2marker = 'X'
             return p1marker,p2marker
        
        
def printboard(positions):
    print('\n'*10)
    print(positions[0]+'|' +positions[1]+ '|'+ positions[2])
    print('-----')
    print(positions[3]+'|' +positions[4]+ '|'+ positions[5])
    print('-----')
    print(positions[6]+'|' +positions[7]+ '|'+ positions[8])

def player1input(positions,p1marker,p2marker):
    printboard(positions)
    p1choice = input("Player 1 select a position to mark")
    if p1choice in positions and int(p1choice) in range(1,10):
        positions[int(p1choice)-1] = p1marker
        nextturn(1,positions,p1marker,p2marker)   
    elif p1choice.upper() == 'Q':
        return
    else:
        printboard(positions)
        player1input(positions, p1marker, p2marker)

def player2input(positions,p1marker,p2marker):
    printboard(positions)
    p2choice = input("Player 2 select a position to mark")
    if p2choice in positions and int(p2choice) in range(1,10):
        positions[int(p2choice)-1] = p2marker
        nextturn(2,positions,p1marker,p2marker)   
    elif p2choice.upper() == 'Q':
        return

    else:
        printboard(positions)
        player1input(positions, p1marker,p2marker)
    
def nextturn(x,positions,p1marker,p2marker):
    if checkhorizons(positions) or checkverts(positions) or checkdias(positions):
        printboard(positions)
        print('Player '+str(x)+' won!')
        restart()
    else:
        if checkstalemate(positions):
            printboard(positions)
            print("Stalemate!")
            restart()
        elif x==1:
            player2input(positions,p1marker,p2marker)
        else:
            player1input(positions,p1marker,p2marker)
        
def checkhorizons(positions):
    for i in range(0,9,3):

        if positions[i] == positions[i+1] and positions[i]==positions[i+2]:
            gamewon = True
            break
        else:
            gamewon = False
    return gamewon


def checkverts(positions):
    for i in range(0,3):
        if positions[i] == positions[i+3] and positions[i] == positions[i+6]:
            gamewon = True
            break
        else:
            gamewon = False
    return gamewon        
        
def checkdias(positions):
    if (positions[0] == positions[4] and positions[0]==positions[8]) or (positions[2] == positions[4] and positions[2]==positions[6]):
        gamewon = True
    else:
        gamewon = False
    return gamewon

def restart():
    newgame = input("New game? (y/n)")
    if newgame in ['n','y']:
        if newgame == 'y':
            startgame()
        else:
            print('Goodbye!')
    else:
        restart()
        
def checkstalemate(positions):
    stalemate = True
    for i in range(1,10):
        for j in positions:
            if str(i) == j:
                stalemate = False
                return stalemate
    return stalemate
        
    
    
startgame()