#!/usr/bin/python3
"""web application listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
