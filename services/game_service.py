from game_logic import Game, Player, add_score
from services import serialize_game, deserialize_game

def create_new_game(username: str, level: str):
    player = Player(username, level)
    game = Game(player, level)
    serialize_game(game)


def add_score_to_highscore():
    game = deserialize_game
    score = game.score
    add_score(score)
    serialize_game(game)


def process_guess(letter: str, game: Game):
    game.round.update(letter)
    game.round.check_for_end()


def wrap_up_game(game: Game):
    score = game.player.wrap_up()
    game.set_score(score)
    serialize_game(game)