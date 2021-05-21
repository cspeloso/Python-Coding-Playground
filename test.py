#   TIC TAC TOE game
#   5/21/2021
import random
import os

clear = lambda: os.system('cls')

gameBoard = [0,0,0,0,0,0,0,0,0]

isUserFinished = False
currentUsersTurn = 1 if random.randint(0,20) <= 10 else 0

print(currentUsersTurn)

while(isUserFinished == False):

    clear()
    print("CURRENT BOARD: ")

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

    
    
