from flask import Flask, request
from flask_cors import CORS, cross_origin

from main import Game

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

game = None

@app.route("/set_difficulty", methods=["POST"])
@cross_origin()
def setDifficulty():
    global game
    data = request.get_json()
    game = Game(data['difficulty'])
    return ""

@app.route("/get_difficulty", methods=["GET"])
@cross_origin()
def getDifficulty():
    global game
    if (not game.started):
        game.started = True
        return {"difficulty": game.level}
    else:
        return "", 500

@app.route("/check_word", methods=["POST"])
@cross_origin()
def checkWord():
    global game
    data = request.get_json()
    if (game.exists(data["word"])):
        return {"check": game.check(data['word'])}
    else:
        return "", 401

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
