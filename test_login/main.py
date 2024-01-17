from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def form_login():
    pass