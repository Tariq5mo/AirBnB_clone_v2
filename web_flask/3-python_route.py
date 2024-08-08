#!/usr/bin/python3
"""web application listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    /python/<text>: display “Python ”, followed by the value of the text variable
    The default value of text is “is cool”.
"""
from flask import Flask
from markupsafe import escape

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
    text = text.replace("_", " ")
    return "C {}".format(escape(text))


@app.route("/python/")
@app.route("/python/<text>")
def Python(text="is cool"):
    formated = text.replace("_", " ")
    return "Python {}".format(formated)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
