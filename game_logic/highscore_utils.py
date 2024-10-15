'''
Highscore utilities for wordguesser.

Variables:
    - HIGHSCORE_PATH: Provides path to highscore.json

Functions:
    - sort_scores(scores): Sorts given scores from highest to lowest.
    - load_highscore(): Loads highscore.json as a dict
    - update_highscore(highscore): writes altered data back to highscore.json
    - is_new_highscore(existing_score, new_score): Compares player scores and 
      determines if the newer score is a highscore. 
    - add_score(score): If the score is the first or better for
      this player at this level, adds the level to the highscore data.
'''

import json
from os import path


HIGHSCORE_PATH = path.join(os.path.dirname(__file__), "..", "data", "highscore.json")


def sort_scores(scores):
    '''
    Sorts scores from highest to lowest.
    - First sorts by time_elapsed (second criterium)
    - Then sorts by pf_ratio (first criterium)
    
    Receives a dict
    Returns a dict
    '''
    
    scores_by_time = sorted(
        scores, 
        key=lambda d: d["time_spent"], 
        reverse=False)
    scores_by_points = sorted(
        scores_by_time, 
        key=lambda d: d["pf_ratio"], 
        reverse=True)
    return scores_by_points


def load_highscore():
    with open(HIGHSCORE_PATH, "r") as f:
        highscore = json.load(f)
    
    #  Sort highscores before returning
    for level, scores in highscore.items():
        highscore[level] = sort_scores(scores)

    return highscore


def update_highscore(highscore):
    with open(HIGHSCORE_PATH, "w") as f:
        json.dump(highscore, f, indent=4)


def is_new_highscore(existing_score, new_score):
    '''
    Compare two player scores and determine if the newer score is a highscore.

    Comparisons:
    - pf_ratio must be higher than the existing score
    - when pf_ratio is equal, time_spent must be lower than the existing score
    - when time_spent is also equal, the earlier date remains highscore so the 
      function returns False.
    
    Returns boolean value.
    '''
    if new_score['pf_ratio'] == existing_score['pf_ratio']:
        if new_score['time_spent'] == existing_score['time_spent']:
            return False
        return new_score['time_spent'] < existing_score['time_spent']
    return new_score['pf_ratio'] > existing_score['pf_ratio']

    
def add_score(score):
    '''
    Formats player score and checks if it needs to be added to highscore data.
    - if a player already has a score at this level, the score is replaced if
      it's higher.
    - if it's the first score for this player at this level, the score is added.
    '''
    highscore = load_highscore()
    level = score.pop("level")
    name = score["name"]
    is_personal_highscore = True
    old_score = None

    for existing_score in highscore[level]:
        if existing_score["name"] == name:
            old_score = existing_score
            is_personal_highscore = is_new_highscore(existing_score, score)
            break

    if is_personal_highscore:
        highscore[level].append(score)
        if old_score != None:
            highscore[level].remove(old_score)
        update_highscore(highscore)







