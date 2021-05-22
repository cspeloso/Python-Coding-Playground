#   TIC TAC TOE game
#   5/21/2021
import random
import os
from sys import platform

if(platform == "win32"):
    clear = lambda: os.system('cls')
elif platform == "darwin":
    clear = lambda: os.system('clear')

gameBoard = [0,0,0,0,0,0,0,0,0]

isUserFinished = False
currentUsersTurn = 1 if random.randint(0,20) <= 10 else 0

print(currentUsersTurn)

while(isUserFinished == False):

    # Clears the board after every turn.
    clear()
    # print("CURRENT BOARD: ")
    # print("| " + gameBoard[0] + " | "  + gameBoard[1] + " | " + gameBoard[2] + " |\n")
    # print("| " + gameBoard[3] + " | "  + gameBoard[4] + " | " + gameBoard[5] + " |\n")
    # print("| " + gameBoard[6] + " | "  + gameBoard[7] + " | " + gameBoard[8] + " |\n")
    print_game_board(gameBoard)
    print(6 % 3)
    print(5 % 3)
    print(4 % 3)

    #   User's turn
    if(currentUsersTurn == 1):
        
        userSelection = input("Please make your move. Enter a valid space number: ")
        
        while(userSelection.isnumeric() == False or int(userSelection) > 9 or int(userSelection) < 1):
            userSelection = input("ERROR: invalid entry detected. Please enter a valid integer: ")

    else:
        userSelection = random.randint(0,8)

        print("Computer's Selection: " + str(userSelection))

        #   if the computer selected an already used space, find another one.
        while(gameBoard[userSelection] != 0):
            userSelection = random.randint(1,9)

    currentUsersTurn = 1 if currentUsersTurn == 0 else 0

    
    

def print_game_board(gameboard):
    for idx, val in gameBoard:
        if(idx % 3 == 0):
            print(val + " |\n")
        else:
            print("| " + val + " | ")