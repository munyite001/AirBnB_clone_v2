#!/usr/bin/python3
"""Run flask Web app
via 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
Route '/hbnb' displays "HBNB"
Route '/c/<text>' displays C <text>
Route '/python/<text>' displays "python <text>"
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C followed by <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def py_text(text="is cool"):
    """prints python followed by <text> content"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if isinstance(n, int):
        if n % 2 == 0:
            val = 'even'
        else:
            val = 'odd'
        return render_template("6-number_odd_or_even.html", n=n, val=val)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
