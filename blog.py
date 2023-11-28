from flask import Flask, render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    user = {"username": "Дениель"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
        {
            "author": {"username": "Ипполит"},
            "body": "Какая гадость эта ваша заливная рыба!!",
        },
    ]

    return render_template("index.html", users=user, posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
