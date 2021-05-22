#   TIC TAC TOE game
#   5/21/2021
import random
import os
from sys import platform

# sets up terminal clear
if(platform == "win32"):
    clear = lambda: os.system('cls')
elif platform == "darwin":
    clear = lambda: os.system('clear')

gameBoard = [ [0,0,0], [0,0,0], [0,0,0] ]
currentTurn = 1
winningPlayer = 0

def HasAnyoneWon():

    global winningPlayer
    
    # check rows
    for i in gameBoard:
        if i[0] == i[1] == [2]:
            if(i[0] == -1):
                print("Player won!")
                winningPlayer = -1
                return True
            elif(i[0] == -2):
                print("Computer won!")
                winningPlayer = -2
                return True
            else:
                return False



    # check if the first column is equal
    if(gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0]):
        if(gameBoard[0][0] == -1):
            print("Player won!")
            winningPlayer = -1
            return True
        elif(gameBoard[0][0] == -2):
            print("Computer won!")
            winningPlayer = -2
            return True
        else:
            return False

    # check if the second column is equal
    if(gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1]):
        if(gameBoard[0][1] == -1):
            print("Player won!")
            winningPlayer = -1
            return True
        elif(gameBoard[0][1] == -2):
            print("Computer won!")
            winningPlayer = -2
            return True
        else:
            return False

    # check if the third column is equal
    if(gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2]):
        if(gameBoard[0][2] == -1):
            print("Player won!")
            winningPlayer = -1
            return True
        elif(gameBoard[0][2] == -2):
            print("Computer won!")
            winningPlayer = -2
            return True
        else:
            return False



    # check if the first diagnol is equal
    if(gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2]):
        if(gameBoard[0][0] == -1):
            print("Player won!")
            winningPlayer = -1
            return True
        elif(gameBoard[0][0] == -2):
            print("Computer won!")
            winningPlayer = -2
            return True
        else:
            return False

    # check if the second diagnol is equal
    if(gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0]):
        if(gameBoard[0][2] == -1):
            print("Player won!")
            winningPlayer = -1
            return True
        elif(gameBoard[0][2] == -2):
            print("Computer won!")
            winningPlayer = -2
            return True
        else:
            return False



    return False

def PrintGameBoard(gameBoard):

    for i in gameBoard:
        spotOne = str("X" if i[0] == -1 else "O" if i[0] == -2 else i[0])
        spotTwo = str("X" if i[1] == -1 else "O" if i[1] == -2 else i[1])
        spotThree = str("X" if i[2] == -1 else "O" if i[2] == -2 else i[2])

        print("| " + spotOne + " | " + spotTwo + " | " + spotThree + " |")

def SetGameboard(selection, user):

    selection = int(selection) - 1

    row = 3 if selection / 3 >= 2 else (2 if selection / 3 >= 1 else 1)
    column = 1 if selection % 3 == 0 else (2 if selection % 3 == 1 else 3)

    gameBoard[row-1][column-1] = -1 if user == -1 else -2
    
def IsSpotTaken(selection):

    selection = int(selection) - 1
    row = 3 if selection / 3 >= 2 else (2 if selection / 3 >= 1 else 1)
    column = 1 if selection % 3 == 0 else (2 if selection % 3 == 1 else 3)

    return True if gameBoard[row-1][column-1] != 0 else False



while(HasAnyoneWon() == False):

    clear()
    PrintGameBoard(gameBoard)

    # Player's Turn
    if(currentTurn == 1):
        
        # get user selection
        userSelection = input("Please select a spot: ")

        # check if the user's selection is invalid
        while(userSelection.isnumeric() == False or int(userSelection) > 9 or int(userSelection) < 1 or IsSpotTaken(userSelection)):
            userSelection = input("ERROR. Please select a correct spot: ")

        # add user selection to game board
        SetGameboard(userSelection, -1)

    # Computer's Turn
    else:

        # get computer selection
        userSelection = random.randint(1,9)

        while(IsSpotTaken(userSelection)):
            userSelection = random.randint(1,9)
        
        SetGameboard(userSelection, -2)

    currentTurn = 2 if currentTurn == 1 else 1
        

clear()
PrintGameBoard(gameBoard)
print("\nPlayer wins!" if winningPlayer == -1 else ("Computer wins!" if winningPlayer == -2 else "It's a draw!"))