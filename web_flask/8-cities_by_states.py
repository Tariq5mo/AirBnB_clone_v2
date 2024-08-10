#!/usr/bin/python3
"""Task8
"""
from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(exception):
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def print_state():
    states_objs = storage.all(State)  # receive all states objects
    return render_template("8-cities_by_states.html", states_objs=states_objs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
