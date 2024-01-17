import sqlite3

db = sqlite3.connect('login.db')
cursor_db = db.cursor()
sql_create = '''create table if not exists Users(
    id integer primary key,
    username text not null,
    password text not null)'''
    
cursor_db.execute(sql_create)

db.commit()
cursor_db.close()
db.close()
