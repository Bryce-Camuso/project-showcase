
class Mancala:

    def __init__(self):
        #1st slot is second players bank. 7th slot is first players bank.
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
        #prints out the board facing player 1
        for i in range(0,8):
            if i == 0 or i == 7:
                print('[  ' + str(self._board[i]) + ' ]')
            else:
                print('[' + str(self._board[i]) + '] ' + '[' + str(self._board[-i]) + '] ' + str(i))



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