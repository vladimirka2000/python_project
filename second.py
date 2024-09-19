from flask import Flask
import random

app = Flask(__name__)


game = ["Орёл", "Решка"]\



def hello_coin():
    return '<a href="/game">Кинуть монетку!</a>'

@app.route("/game")

def coin_game():
    return f'<p>{random.choice(game)}</p>'



app.run(debug=True)

