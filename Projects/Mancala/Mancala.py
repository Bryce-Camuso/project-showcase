
class Mancala:

    def __init__(self):
        '''
        This class expects 0 inputs. The board is represented as an array were slots 1-6 are player 1 and 8-13 are player 2 with 13 = 1 in the print method (see below). Slots 0 is player 2's goal and slot 7 is player 1's goal.

          [  0  ] <-- Player 2's goal
        1 [4] [4] 13 (1)
        2 [4] [4] 12 (2)
        3 [4] [4] 11 (3)
        4 [4] [4] 10 (4)
        5 [4] [4] 9  (5)
        6 [4] [4] 8  (6)
          [  0  ] <-- Player 1's goal
        '''
        self._board = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]

    def _valid_move(self, index, player):
        if index < 0 or index > 14:
            return False
        elif self._board[index] == 0:
            return False
        elif index == 0 or index == 7:
            return False
        elif (index > 8 and player == 1) or (index < 7 and player == 2):
            return False
        else:
            return True

    def move(self, index, player):
        '''
        This method takes the index of the board array representing the player's move and which player represented as 1 or 2 for player 1 and player 2.
        
        This method returns a tuple of bool values. The first value represents if the move was successful. The second represents if the player received an extra turn.
        '''
        #First return condintional signles that the move was succsesful. The second return condintional specifies if the person getts another turn.
        #check for valid moves
        if not self._valid_move(index, player):
            return False, False
        
        #set up variables
        counter = self._board[index]
        self._board[index] = 0
        slot = index + 1
        #move around the board placing one marble until the pile/counter is empty
        while counter > 0:
            if slot > 13:
                slot = 0
            if (slot == 0 and player == 2) or (slot == 7 and player == 1):
                self._board[slot] += 1
            elif slot == 0 or slot == 7:
                counter += 1
            else:
                self._board[slot] += 1
            slot += 1
            counter -= 1
        #if the last slot was the persons goal they get an extra turn.
        if slot - 1 == 0 or slot - 1 == 7:
            return True, True
        return True, False
    


    def _player_collect(self, player):
        collection = 0
        #get what slots need to be added up
        if player == 1:
            start = 1
            end = 6
        else:
            start = 8
            end = 13
        #go through the piles to collect any remainding marbles to put in the persons goal
        for i in range(start, end):
            collection += self._board[i]
        if player == 1:
            self._board[7] += collection
        
        else:
            self._board[0] += collection


    def _winner(self):
        if self._board[0] > self._board[7]:
            print('player 2 wins')
        else:
            print('player 1 wins')

        print(str(self._board[7]) + ' = ' + str(self._board[0]))

    def end_of_game(self):
        '''
        
        This method checks if the game has ended. If one side is left with 0 marbles the game is considered over. If found to be true the class will total the remaining marbles on the board and give them to the associated player. Once complete it will print out the winner and final score.

        This method will return True if the game has ended and False otherwise.
        '''
        player1 = True
        player2 = True
        #checks if either player has no marbles left.
        for i in range(1,7):
            if self._board[i] > 0:
                player1 = False
            if self._board[-i] > 0:
                player2 = False
        #if someone has no marbles game ends and the other person gets any marbles on their side
        if player1 == True:
            self._player_collect(2)

        elif player2 == True:
            self._player_collect(1)

        #check for the if the game ended
        if player1 == True or player2 == True:
            self._winner()
            return True
        else:
            return False

    def print_board(self):
        '''
        This method prints out the board with player 2's goal on the top and player 1's goal on the bottom . Player 1 is on the left with marbles moving down. Player 2 is on the right with marbles moveing up. Player 1's slots are 1-6 as printed. Player 2's slots are 8-13 with 13 = 1 in the print out (see below).

          [  0  ] <-- Player 2's goal
        1 [4] [4] 13 (1)
        2 [4] [4] 12 (2)
        3 [4] [4] 11 (3)
        4 [4] [4] 10 (4)
        5 [4] [4] 9  (5)
        6 [4] [4] 8  (6)
          [  0  ] <-- Player 1's goal
        '''
        for i in range(0,8):
            if i == 0:
                print('  [  ' + str(self._board[i]) + '  ] <-- Player 2\'s goal')
                
            elif i == 7:
                print('  [  ' + str(self._board[i]) + '  ] <-- Player 1\'s goal')
            
            else:
                print(str(i) + ' [' + str(self._board[i]) + '] ' + '[' + str(self._board[-i]) + '] ' + str(i))



def _test():
    game = Mancala()
    game.print_board()
    game.move(1,1)
    game.move(2,1)
    game.move(3,1)
    game.move(4,1)
    game.move(5,1)
    game.move(6,1)
    game.move(1,1)
    game.move(2,1)
    game.move(3,1)
    game.move(4,1)
    game.move(5,1)
    game.move(6,1)
    game.print_board()
    game.end_of_game()


if __name__ == '__main__':
    _test()