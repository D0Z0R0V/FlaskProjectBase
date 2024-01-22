import os
import sqlite3

connection = sqlite3.connect('todo/app.db')

with open('todo/schema.sql', 'r') as sq:
    connection.executescript(sq.read())

cursor_db = connection.cursor()

connection.commit()
connection.close()

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "the secret key"