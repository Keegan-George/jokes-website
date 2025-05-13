"""
A website that queries a new joke, from the Joke API, each time the clown image is clicked.
"""

from joke import get_joke
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        joke = get_joke()
        return render_template("index.html", joke=joke)

    return render_template("index.html", joke=None)


if __name__ == "__main__":
    app.run(debug=True)
