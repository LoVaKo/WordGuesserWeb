'''
Functions:
    - deserialize_game: Deserializes game state using pickle.
    - serialize_game: Serializes game state using pickle .
'''
import pickle
from flask import session
from game_logic import Game


def deserialize_game():
    game_state = session.get("game_state")
    return pickle.loads(game_state)


def serialize_game(game: Game):
    session["game_state"] = pickle.dumps(game)