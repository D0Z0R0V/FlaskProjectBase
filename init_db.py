import sqlite3

connection = sqlite3.connect("db_app.db")

with open("sql_schema.sql") as f:
    connection.executescript(f.read())

cur = connection.cursor()

connection.commit()
connection.close()