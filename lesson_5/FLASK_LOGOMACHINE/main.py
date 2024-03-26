from flask import Flask, request, jsonify


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


# http://127.0.0.1:5000/NUMBER_ONE/NUMBER_TWO/OPERATION


@app.route("/<NUMBER_ONE>/<NUMBER_TWO>/<OPERATION>")
def operation(NUMBER_ONE: str, NUMBER_TWO: str, OPERATION: str):
    NUMBER_ONE, NUMBER_TWO = float(NUMBER_ONE.replace(',', '.')), float(NUMBER_TWO.replace(',', '.'))
    if OPERATION == '+':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE + NUMBER_TWO}'
    elif OPERATION == '-':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE - NUMBER_TWO}'
    elif OPERATION == '*':
        return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE * NUMBER_TWO}'
    elif OPERATION == ':':
        if NUMBER_TWO == 0:
            return "На ноль делить нельзя"
        else:
            return f'{NUMBER_ONE} {OPERATION} {NUMBER_TWO} = {NUMBER_ONE / NUMBER_TWO}'
    else:
        return 'В URL указана неверная арифметическая операция'


# http://127.0.0.1:5000/hello?name=Petr&surname=Ivanov
@app.route("/hello")
def hello():
    name: str = request.args.get("name", "HELLO")
    surname: str = request.args.get("surname", "WORLD")
    return f'Hello {name} {surname}'


def get_all_users_from_db():
    return [
        {
            "id": 1,
            "username": "alex223190",
            "email": "alex_sidorov@gmail.com"
        },
        {
            "id": 23,
            "username": "petr22111965",
            "email": "petr_voronin@mail.ru"
        }
    ]


@app.route("/users")
def get_users():
    users: list = []
    for user in get_all_users_from_db():
        users.append(user)
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)