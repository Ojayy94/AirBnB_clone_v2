#!/usr/bin/python3
"""A script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000

Routes:
/: display "Hello HBNB!"

You must use the option strict_slashes=False in your route definition
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home_hbnb():
    """To display "Hello HBNB!"
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """To display "Hello HBNB!"
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """display 'C' followed by the value of the text
       variable (replace underscore _ symbols with a space )
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/(<text>)/" strict_slashes=False)
def python(text="is cool"):
    """display 'Python', followed by the value of the text variable
       (replace underscore _ symbols with a space )
       The default value of text is 'is cool'
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run('0.0.0.0')
