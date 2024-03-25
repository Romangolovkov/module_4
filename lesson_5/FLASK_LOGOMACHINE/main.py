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


if __name__ == "__main__":
    app.run()