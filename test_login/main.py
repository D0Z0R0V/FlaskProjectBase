from flask import Flask, request, render_template, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('login.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/login', methods=['GET', 'POST'])
def form_login():
    if request.method == "POST":
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        
        db = get_db_connection()
        cursor_db = db.execute(('''SELECT password FROM Users WHERE username = "{}"''').format(Username))
        
        pas = cursor_db.fetchall()
        cursor_db.close()
        
        try: 
            if pas[0][0] != Password:
                return render_template('bad_auth.html')
        except:
            return render_template('bad_auth.html')
        
        db.close()
        return render_template('successful.html')
    
    return render_template('author.html')


@app.route('/reqist', methods=['POST', 'GET'])
def regist():
    if request.method == "POST":
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        
        db = get_db_connection()
        db.execute("INSERT INTO Users (username, password) VALUES( ?, ?)", (Username, Password))
        db.commit()
        db.close()
        
        return render_template('successful.html')
    
    return render_template('regist.html')


if __name__ == "__main__":
    app.run(debug=True)