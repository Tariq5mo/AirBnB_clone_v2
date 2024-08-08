#!/usr/bin/python3
"""web application listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
"""
from flask import Flask

web_flask1 = Flask(__name__)


@web_flask1.route("/", strict_slashes=False)
def web_flask():
    """ Print simple sentence """
    return "Hello HBNB!"

if __name__ == "__main__":
    web_flask1.run(host="0.0.0.0", port=5000)
