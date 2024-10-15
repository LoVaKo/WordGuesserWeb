'''
Game module for wordguesser.

Class Game: 
    - Initialized with Player instance and level.
    - The game runs for 10 rounds.
    - After 10 rounds have been played the player's score is stored.

Functions:
    - __init__(self, player): Initializes new game for given player.
    - set_score(self, score): Stores player score
    - new_round(self): Initializes new Round and increases the counter.
'''
from .round import Round

class Game:
    
    def __init__(self, player, level):
        self.player = player
        self.level = level
        self.round_counter = 0
        self.score = None
        self.round = None
        
    def set_score(self, score):
        self.score = score

    def new_round(self):
            self.round = Round(self.player, self.level)
            self.round_counter += 1
        
        


