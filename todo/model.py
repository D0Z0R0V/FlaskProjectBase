import os
import sqlite3

db_path = os.path.abspath('app.db')
connection = sqlite3.connect(db_path)

with open('schema.sql', 'r') as sq:
    connection.executescript(sq.read())

cursor_db = connection.cursor()

connection.commit()
connection.close()