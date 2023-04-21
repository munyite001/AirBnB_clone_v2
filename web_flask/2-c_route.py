#!/usr/bin/python3
"""Run flask Web app
via 0.0.0.0:5000
Route '/' displays "Hello HBNB!"
Route '/hbnb' displays "HBNB"
Route 'c/<text>' displays C <text>

"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns 'HBNB'"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """ Returns 'C <text>'"""
    text = text.replace('_', ' ')
    return f"C %s" % text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
