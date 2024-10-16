'''
Flask application for WordGuesser game. It allows the user to view the
Highscore or to start a new game, choosing from 5 difficulty levels.
The players' score can be stored in the highscore file.
The game state is serialized and stored in a Redis-backed session.

Functions:
    - deserialize_game: Deserializes game state using pickle.
    - serialize_game: Serializes game state using pickle .

Routes:
    /:          GET:    Render home page.
    /new_game   GET:    Render page that prompts the user to fill in their user 
                        name and pick a difficulty level.
                POST:   Initializes a new game and calls gameplay().
    /highscore: GET:    Render highscore page.
                POST:   Optionally adds player score and renders highscore page.
    /gameplay:  POST:   Play the game by guessing letters and moving through
                        rounds.
'''
from flask import Flask, render_template, request, session
from flask_session import Session
import redis
import pickle
from game_logic import Player, Game, load_highscore, add_score

app = Flask(__name__)

#  Configure Flask app to use Redis for session storage
SESSION_TYPE = "redis"
SESSION_PERMANENT = False
SESSION_REDIS = redis.StrictRedis(host="localhost", port=6379)
app.config.from_object(__name__)
Session(app)


def deserialize_game():
    game_state = session.get("game_state")
    return pickle.loads(game_state)


def serialize_game(game: Game):
    session["game_state"] = pickle.dumps(game)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/new_game", methods=["POST", "GET"])
def new_game():
    '''
    GET:    Render a form to start a new game.
    POST:   Create new Player and Game instances, serialize the game, 
            and starts the game by redirecting to the gameplay page.
    '''
    if request.method == "POST":
        username = request.form.get("username")
        level = request.form.get("level")

        player = Player(username, level)
        game = Game(player, level)
        serialize_game(game)

        return gameplay()
    
    return render_template("new_game.html")


@app.route("/highscore", methods=["POST", "GET"])
def highscore():
    '''
    GET:    Render highscore page.
    POST:   Optionally add player score to the highscore before rendering it.
    '''
    if request.method == "POST":
        add_to_highscore = request.form.get("highscore")
        if add_to_highscore == "yes":
            game = deserialize_game()
            score = game.score
            add_score(score)
            serialize_game(game)

    highscore = load_highscore()
    return render_template("highscore.html", highscore=highscore)

    
@app.route("/guess_letter", methods=["POST", "GET"])
def gameplay():
    '''
    -   Prompt the user to pick a letter. 
    -   If a letter has been guessed, resolve the guess. 
    -   Checks end of round conditions: If the round is not over, render the
        game page.
    -   If the round is over, initialize a new round and start it.
    -   If 10 rounds have been played, wrap up the player score en render the
        finished page.
    '''
    game = deserialize_game()
    letter = request.form.get("letter")

    if letter:
        game.round.update(letter)
        game.round.check_for_end()
        if game.round.game_over is False:
            serialize_game(game)
            return render_template("gameplay.html", game=game)

    if game.round_counter < 10:
        game.new_round()
        serialize_game(game)
        return render_template("gameplay.html", game=game)
    
    score = game.player.wrap_up()
    game.set_score(score)
    serialize_game(game)

    return render_template("finished.html", game=game)


if __name__ == "__main__":
    app.run()
