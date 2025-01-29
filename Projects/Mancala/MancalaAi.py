from Mancala import Mancala
from Tree import NAryTree
import random

class MancalaAi(Mancala):



    def __init__(self):
        super().__init__()
        #Easy is level 0 Medium is level 1 Hard is level 3
        self._level = None
        notPicked = True
        self._playtree = NAryTree(6)
        while notPicked:
            print('What level of AI would you like to use? (Easy, Medium, or Hard)')
            playerInput = input().lower()
            if playerInput == 'easy' or playerInput == '2':
                self._level = 0
            elif playerInput == 'medium' or playerInput == 'm':
                self._level = 1
            elif playerInput == 'hard' or playerInput == 'h':
                self._level = 2              
            else:
                print("invalid input")
            if self._level is not None:
                notPicked = False


    def _easy(self):
        return random.randint(8, 13)
    
    def _extra_turn_check(self):
        numberCheck = 1
        #check if the AI can gain an extra turn
        for i in range(13,7, -1):
            if self._board[i] == numberCheck:
                return i
            else:
                numberCheck += 1
            
    
    def _score_point(self):
        numberCheck = 7
        for i in range(8, 14):
            if self._board[i] >= numberCheck:
                return i
            else: 
                numberCheck -= 1


    def _medium(self):
        move = None

        move = self._extra_turn_check()
        if move is None:
            move = self._score_point()
        if move is None:
            move = random.randint(8, 13)

        return move

    def _test_move(self, index, player, trueBoard):
        if trueBoard[index] == 0:
            return False, False, trueBoard
        board = trueBoard.copy()
        counter = board[index]
        board[index] = 0
        slot = index + 1
        #move around the board placing one marble until the pile/counter is empty
        while counter > 0:
            if slot > 13:
                slot = 0
            if (slot == 0 and player == 2) or (slot == 7 and player == 1):
                board[slot] += 1
            elif slot == 0 or slot == 7:
                counter += 1
            else:
                board[slot] += 1
            slot += 1
            counter -= 1
        
        if slot - 1 == 0 or slot - 1 == 7:
            return True, True, board
        
        return True, False, board
    
    def _posible_player_moves(self, Opturns, node):
        #print(node.get_element())
    
        for i in range(1,7):
            validMove, extraTurn, newBoard = self._test_move(i, 1, node.get_element())
            if validMove and extraTurn:
                node.set_children(NAryTree(6,newBoard, node), i - 1)
                self._posible_player_moves(Opturns, node.get_child(i- 1))

            elif validMove:
                node.set_children(NAryTree(6,newBoard, node), i  - 1)
                self._posible_moves(Opturns - 1, node.get_child(i - 1))

        #look for the minimum possible value of all the positions to propigate as the oponets turn.
        mixValue = float('inf')
        for x in node.get_children():
            if x is not None and mixValue > x.get_element():
                mixValue = x.get_element()
        node.set_element(mixValue)
        


    def _posible_moves(self, Opturns, node):
        '''not taking into account oponets turn. use extraTurn to add leves and count player turns'''
        #lookes through all moves in this position while taking into account 
        if Opturns > 0:
            for i in range(8,14):
                validMove, extraTurn, newBoard = self._test_move(i, 2, node.get_element())
                if validMove and extraTurn:
                    #(7 - (i % 7)) - 1 is used to as the move is considered 1-6 while the array is 0-5 with 13 = move 1. Thus 13 % 7 = 6 & 7-6 = 1. so move 1 is slot 0 in the tree array
                    node.set_children(NAryTree(6,newBoard, node), (7 - (i % 7)) - 1)
                    self._posible_moves(Opturns, node.get_child(7 - (i % 7) - 1))

                elif validMove:
                    node.set_children(NAryTree(6,newBoard, node), (7 - (i % 7)) - 1)
                    self._posible_player_moves(Opturns, node.get_child((7 - (i % 7)) - 1))
        
        #once at the end get the final score as the positions value and set it to the node's element. Else it is not the end and then we are looking for the max score among the positions.
        if Opturns == 0:
            board = node.get_element()
            node.set_element(board[0] - board[7])

        else:
            maxValue = float('-inf')
            for x in node.get_children():
                if x is not None and maxValue < x.get_element():
                    maxValue = x.get_element()
            node.set_element(maxValue)
        


    def _hard(self):
        self._playtree = NAryTree(6)
        self._playtree.set_element(self._board)
        self._posible_moves(2, self._playtree)
        maxScore = float('-inf')
        index = 0
        for i in range(0,6):
            if self._playtree.get_child(i) is not None and maxScore < self._playtree.get_child(i).get_element():
                maxScore = self._playtree.get_child(i).get_element()
                index = i
        end = index + 1
        index = 14
        for i in range(0, end):
            index -= 1
        
        return index

    
    def ai_move(self):
        aiMove = None
        validMove = False
        extraTurn = False
        while not validMove:
            if self._level == 0:
                aiMove = self._easy()
            elif self._level == 1:
                aiMove = self._medium()
            else:
                aiMove = self._hard()
                #print(aiMove)
            validMove, extraTurn = self.move(aiMove, 2)

        return 7 - (aiMove % 7), extraTurn



def _print_tree(node, level):
    if node is not None and level < 2:
        print('----------------------------------------------')
        print('level = ' + str(level))
        if node.get_parent() is not None:
            print('parent = ' + str(node.get_parent().get_element()))
        print(node.get_element())
        for i in range (0,6):
                _print_tree(node.get_child(i), level + 1)
    

def _test():
    game = MancalaAi()

    game.move(3,1)
    game.move(6,1)

    game._hard()

    _print_tree(game._playtree, 0)


if __name__ == '__main__':
    _test()