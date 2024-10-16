'''
Routes for Flask app WordGuesserWeb
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

from flask import Blueprint, render_template, request
from services import create_new_game, add_score_to_highscore, process_guess, deserialize_game, serialize_game, wrap_up_game
from game_logic import load_highscore

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/")
def home():
    return render_template("home.html")


@routes_bp.route("/new_game", methods=["POST", "GET"])
def new_game():
    if request.method == "POST":
        username = request.form.get("username")
        level = request.form.get("level")
        create_new_game(username, level)
        return gameplay()
    
    if request.method == "GET":
        return render_template("new_game.html")


@routes_bp.route("/highscore", methods=["POST", "GET"])
def highscore():
    '''
    GET:    Render highscore page.
    POST:   Optionally add player score to the highscore before rendering it.
    '''
    if request.method == "POST":
        add_to_highscore = request.form.get("highscore")
        if add_to_highscore == "yes":
            add_score_to_highscore()

    highscore = load_highscore()
    return render_template("highscore.html", highscore=highscore)

    
@routes_bp.route("/guess_letter", methods=["POST", "GET"])
def gameplay():
    '''
    -   Prompt the user to pick a letter. 
    -   If a letter has been guessed, process the guess. 
    -   Checks end of round conditions: If the round is not over, render the
        game page.
    -   If the round is over, initialize a new round and start it.
    -   If 10 rounds have been played, wrap up the player score en render the
        finished page.
    '''
    letter = request.form.get("letter")
    game = deserialize_game()

    if letter:
        process_guess(letter, game)
        if game.round.game_over is False:
            serialize_game(game)
            return render_template("gameplay.html", game=game)

    if game.round_counter < 10:
        game.new_round()
        serialize_game(game)
        return render_template("gameplay.html", game=game)
    
    wrap_up_game(game)

    return render_template("finished.html", game=game)