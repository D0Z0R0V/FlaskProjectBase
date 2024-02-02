CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL 
);

CREATE TABLE IF NOT EXISTS ToDo_Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT CHECK(length(title) <= 100),
    is_complete BOOLEAN,
    user_id text NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (id)
);
