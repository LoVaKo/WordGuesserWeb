'''
Player module for wordguesser.

class Player:
    - Initialized with name and level before starting a game.
    - Instance data is used to update the game highscore.
    
Functions:
    - __init__(self, name, level): Initializes a new player instance.
    - add_fail(self): Increases fails with 1.
    - add_point(self): Increases points with 1. 
    - calculate_pf_ratio(self): Calculates the ratio between points and fails.
    - calculate_time_spent(self): Calculates the time spent playing the game.
    - format_date(self): Formats the datetime object to "10-05-22"
    - format_player_stats(self): Creates a dictionary from instance attributes,
      and removes unneccesary information.
    - wrap_up(self): Prepares player data and returns formatted player stats.
'''
from datetime import datetime

class Player:

    def __init__(self, name, level):
        self.name = name
        self.date = datetime.now()
        self.points = 0
        self.fails = 0
        self.pf_ratio = 0
        self.time_spent = 0
        self.level = level
    
    def add_fail(self):
        self.fails += 1
    
    def add_point(self):
        self.points += 1
    
    def calculate_pf_ratio(self):
        if self.fails == 0: 
            self.pf_ratio = "10.0"  #  Prevent ZeroDevisionError
            return
        self.pf_ratio = str(round(self.points / self.fails, 1))
    
    def calculate_time_spent(self):
        finish_time = datetime.now()
        elapsed_time = finish_time - self.date
        self.time_spent = str(elapsed_time)  
    
    def format_date(self):
        self.date = self.date.strftime('%d-%m-%y')
    
    def format_player_stats(self):
        '''
        - Create a dictionary from the player instance attributes.
        - Remove redundant information (points and fails since there is a
          point/fail ratio included).
        - Return dict.
        '''
        player_stats = vars(self)
        player_stats.pop('points')
        player_stats.pop('fails')
        return player_stats

    def wrap_up(self):
        self.calculate_pf_ratio()
        self.calculate_time_spent()
        self.format_date()
        return self.format_player_stats()
        
    