#!/usr/bin/python3
"""
Flask web server
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Hello route
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB route
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """
    C route
    """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """
    Python route
    """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    Number routej
    """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Number template route
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Number odd or even route
    """
    parity = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, p=parity)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    List all states
    """
    return render_template("7-states_list.html", states=storage.all(State))


@app.teardown_appcontext
def remove_sql_session(exception):
    """
    Remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
