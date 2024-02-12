CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL 
);

CREATE TABLE ToDo_Users (
    todo_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    title TEXT NOT NULL,
    completed BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id)
);
