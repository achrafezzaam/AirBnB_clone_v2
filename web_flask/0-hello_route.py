#!/usr/bin/python3
''' Start a flask app listening to all IP's at port 5000 '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    ''' Display the message Hello HBNB! '''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
