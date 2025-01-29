from Mancala import Mancala
from MancalaAi import MancalaAi
import random


def AI_game_loop():
    #set up Ai and variables
    game =  MancalaAi()
    playerInput = None
    while not game.end_of_game():
        print("What would you like to do?")
        game.print_board()
        playerInput = int(input())

        validMove, extraTurn = game.move(playerInput, 1)
        if validMove == False:
            print('invalid move please retry.')

        elif extraTurn:
            print("You got an extra turn!")
        else:
            extraTurn = True
            while extraTurn:
                aiMove, extraTurn = game.ai_move()
                print('AI\'s move is: ' + str(aiMove))
                if extraTurn:
                    print('AI got and extra turn.')


def two_player_game_loop():
    #set up variables using the mancala class
    game = Mancala()
    turn = 1
    playerInput = None
    #while the game has not ended continue the while loop. Checks each input to see if the game has been ended.
    while not game.end_of_game():
        #print UI
        print("player " + str(turn) + " what would you like to do?")
        game.print_board()
        playerInput = int(input())
        #game handles discrepancy between the Class array and player choise. Class expects the array slot you choose.
        if turn == 2:
            end = playerInput
            playerInput = 14
            for i in range(0, end):
                playerInput -= 1
        #makes a move if valid else the class returns false to signle it did nothing.
        validMove, extraTurn = game.move(playerInput, turn)
        if validMove and not extraTurn:
            if turn == 1:
                turn = 2
            else:
                turn = 1
        elif extraTurn:
            print("player " + str(turn) + " got an extra turn!")

        else:
            print('invalid move please retry.')

    










print('Would you like to play Mancala with 1 or 2 players? (1 or 2)')
playerInput = input()
if playerInput == '2':
    two_player_game_loop()
else: 
    AI_game_loop()