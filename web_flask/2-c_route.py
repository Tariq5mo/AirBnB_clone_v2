#!/usr/bin/python3
"""web application listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Print simple sentence """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ Print simple sentence """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ Print simple sentence """
    if isinstance(text, str):
        text = str(text).replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
