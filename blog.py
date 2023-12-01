from flask import Flask, render_template, flash, redirect, url_for
from config import Config
from form import LoginForm
#from flask_migrate import Migrate

import sqlite3

app = Flask(__name__)
app.config.from_object(Config)


def get_db_connection():
    conn = sqlite3.connect("db_app.db")
    conn.row_factory = sqlite3.Row
    return conn


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


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(
            "Login requested for user {}, remember_me={}".format(
                form.username.data, form.remember_me.data
            )
        )
        return redirect(url_for("index"))
    return render_template("login.html", form=form, title="Sign In")


if __name__ == "__main__":
    app.run(debug=True)
