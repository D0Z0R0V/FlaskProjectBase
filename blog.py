from flask import Flask, render_template

app = Flask(__name__)


@app.routes('/')
def index():
    return render_template('index.html')