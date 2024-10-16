'''
Flask application for WordGuesser game. It allows the user to view the
Highscore or to start a new game, choosing from 5 difficulty levels.
The players' score can be stored in the highscore file.
The game state is serialized and stored in a Redis-backed session.
'''
from flask import Flask
from flask_session import Session
import redis
from controllers import routes_bp

app = Flask(__name__)

#  Configure Flask app to use Redis for session storage
SESSION_TYPE = "redis"
SESSION_PERMANENT = False
SESSION_REDIS = redis.StrictRedis(host="localhost", port=6379)
app.config.from_object(__name__)
Session(app)
app.register_blueprint(routes_bp)

if __name__ == "__main__":
    app.run()
