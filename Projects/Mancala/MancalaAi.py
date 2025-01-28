from Mancala import Mancala
import random

class MancalaAi(Mancala):

    def __init__(self):
        super().__init__()
        #Easy is level 0 Medium is level 1 Hard is level 3
        self._level = None
        notPicked = True
        while notPicked:
            print('What level of AI would you like to use? (Easy, Medium, or Hard)')
            playerInput = input().lower()
            if playerInput == 'easy':
                self._level = 0
            elif playerInput == 'medium':
                self._level = 1
            elif playerInput == 'hard':
                self._level = 2
            else:
                print("invalid input")
            if self._level is not None:
                notPicked = False


    def easy(self):
        return random.randint(8, 13)
    
    def medium(self):
        pass

    def hard(self):
        pass
    
    def ai_move(self):
        aiMove = None
        validMove = False
        while not validMove:
            if self._level == 0:
                aiMove = self.easy()
            elif self._level == 1:
                aiMove = self.medium()
            else:
                aiMove = self.hard()
            validMove = self.move(aiMove, 2)

        return 7 - (aiMove % 7)

