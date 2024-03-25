from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


# http://127.0.0.1:5000/world


@app.route("/world")
def world():
    return """
    Под мартовскими лучами солнца тает снег.
    В оттаевшей земле начинает всходить первая зелень.
    Природа начинает просыпаться после зимней спячки    
"""


@app.route("/<NUMBER_ONE>/<NUMBER_TWO>/<OPERATION>")
def operation(NUMBER_ONE: str, NUMBER_TWO: str, OPERATION: str):
    NUMBER_ONE, NUMBER_TWO = float(NUMBER_ONE), float(NUMBER_TWO)
    if OPERATION == '+':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE + NUMBER_TWO}'
    elif OPERATION == '-':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE - NUMBER_TWO}'
    elif OPERATION == '*':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE * NUMBER_TWO}'
    elif OPERATION == ':':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE / NUMBER_TWO}'
    else:
        return 'В URL указана неверная арифметическая операция'


if __name__ == "__main__":
    app.run()