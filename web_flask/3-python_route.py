#!/usr/bin/python3
''' Start a flask app listening to all IP's at port 5000 '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    ''' Display the message Hello HBNB! '''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    ''' Display the message HBNB '''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    ''' Build a string from the route parameter '''
    return "C " + text.replace("_", " ")


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    ''' Build a string from the route parameter. if the parameter
        is missing, display the message: Python is cool '''
    return "Python " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
