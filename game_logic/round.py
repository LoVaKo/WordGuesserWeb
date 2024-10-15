'''
Round module for wordguesser.

Variables:
    - _possible_words: List of seven letter words

Functions:
    - generate_random_word(): Function that picks a random word from the list.
class Round:
    - Initialized with player and level
    - Level determines number of tries.
    - The round ends when:
        - Number of tries reaches zero.
        - All letters of the word have been guessed.
    - When the round ends the player stats are updated.

Methods:

    - __init__(self, player, level): Initializes a new round.
    - check_for_end(self): Checks for end of round conditions.
    - update(self, guess): Updates the gameboard or number of tries.
'''
import random as rd

_possible_words = [
            "abandon", "baggage", "cabinet", "dancing", "passion",
            "fantasy", "giraffe", "harmony", "imagery", "jackets",
            "kitchen", "languid", "magical", "narrate", "octopus",
            "package", "quizzes", "rainbow", "diamond", "example",
            "unicorn", "victory", "writers", "xylitol", "yawning",
            "zealous", "ability", "bizarre", "courage", "decline",
            "exhibit", "factors", "genuine", "heavens", "improve",
            "journey", "kingdom", "ladders", "mystery", "nostalg",
            "optimal", "precise", "qualify", "respect", "stamina",
            "triumph", "upwards", "vintage", "whisper", "xylomas",
            "yankees", "zephyrs", "artwork", "brother", "curious",
            "dormant", "elevate", "fragile", "glimpse", "hustler",
            "insight", "justice", "kitchen", "lighten", "modesty",
            "neither", "opinion", "puzzles", "quantum", "remains",
            "silence", "tackled", "uniform", "venture", "warrior",
            "yearned", "zealots", "arrange", "balance", "capture",
            "dolphin", "embrace", "fiction", "gravity", "horizon",
            "insider", "justice", "knights", "lasting", "machine",
            "network", "orchids", "plastic", "quality", "remorse",
            "service", "tangent", "updates", "vibrate", "whistle"
        ]


def generate_random_word():
    random_number = rd.randint(0, 99)
    return _possible_words[random_number]


class Round:
    
    def __init__(self, player, level):
        self.word = Round.generate_random_word()
        self.board = ['_', '_', '_', '_', '_', '_', '_']
        self.guessed_letters = []
        self.game_over = False
        self.player = player
        self.level = level
        match level:
            case "Beginner": self.tries = 7
            case "Easy": self.tries = 6
            case "Medium": self.tries = 5
            case "Hard": self.tries = 4
            case "Expert": self.tries = 3
    
    def check_for_end(self):
        if self.tries == 0:
            self.game_over = True
            self.player.add_fail()
            return
        if '_' not in self.board: 
            self.game_over = True
            self.player.add_point()
    
    def update(self, guess):
        self.guessed_letters.append(guess)

        if guess not in self.word:
            self.tries -= 1
            return
        
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.board[index] = letter


