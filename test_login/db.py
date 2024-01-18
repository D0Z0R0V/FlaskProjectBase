import sqlite3

connection = sqlite3.connect('login.db')

with open('schema.sql', 'r') as sq:
    connection.executescript(sq.read())

cursor_db = connection.cursor()

connection.commit()
connection.close()
