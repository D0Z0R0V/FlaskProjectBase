import sqlite3

connection = sqlite3.connect('app.db')

with open('schema.sql', 'r') as sq:
    connection.executescript(sq.read())

cursor_db = connection.cursor()

connection.commit()
connection.close()