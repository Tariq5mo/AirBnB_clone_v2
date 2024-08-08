#!/usr/bin/python3
"""
Add the route:
/number_template/<n>: display a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY.
"""
from flask import Flask, render_template
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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>")
def Python(text="is cool"):
    formated = text.replace("_", " ")
    return "Python {}".format(formated)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
