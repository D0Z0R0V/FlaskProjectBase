import requests
import sqlite3
import os
from flask import Flask, render_template, request, url_for, redirect, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import abort
from todo.config import Config


app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    db_path = os.path.abspath('todo/app.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def get_post(todo_id):
    db = get_db_connection()
    post = db.execute("SELECT * FROM ToDo_Users WHERE id = ?", (todo_id,)).fetchone()
    db.close()
    
    if post is None:
        return abort(404)
    return post


def get_weather_data(city):
    appid = "f6ae488f0ab8f3b69469ef0f66452b1b"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=".format(
            city
        )
        + appid
    )

    response = requests.get(url)
    weather_data = response.json()

    if response.status_code != 200:
        return None

    return weather_data


@app.route('/', methods=['GET', 'POST'])
def form_login():
    if request.method == "POST":
        Username = request.form.get('Username')
        Password = request.form.get('Password')
        session["username"] = Username
        
        db = get_db_connection()
        cursor_db = db.execute('SELECT password FROM Users WHERE username = ?',(Username,))
        
        pas = cursor_db.fetchone()[0]
        cursor_db.close()
        
        try: 
            if not check_password_hash(pas, Password):
                return render_template('login/bad_auth.html')
        except:
            return render_template('login/bad_auth.html')
        
        db.close()
        return render_template('login/successful.html')
    
    return render_template('login/author.html')


@app.route('/reqist', methods=['POST', 'GET'])
def regist():
    if request.method == "POST":
        Username = request.form.get('Username')
        Password = generate_password_hash(request.form.get('Password'))
        
        db = get_db_connection()
 
        db.execute("INSERT INTO Users (username, password) VALUES( ?, ?)", (Username, Password))
        db.commit()
        db.close()
        
        return render_template('login/successful_copy.html')
    
    return render_template('login/regist.html')


@app.route('/logout')
def logout():
    session.clear() 
    return redirect(url_for('form_login'))


@app.get("/todo")
def home():
    db = get_db_connection()
    
    todo_list = db.execute('SELECT * FROM ToDo_Users').fetchall()
    db.close()
    username = session.get("username", "DoZorov")
    return render_template("index.html", todo_list=todo_list, username=username, title="Главная страница")


@app.post("/add")
def add():
    title = request.form.get("title")
    complete = request.form.get("completed", type=bool) == False
    
    if not title:
        flash("Добавьте название задачи!")
    else:
        db = get_db_connection()      
        db.execute("INSERT INTO ToDo_Users (title, completed) VALUES (?, ?)",(title, complete))
        db.commit()
        db.close()
        
    return redirect(url_for("home"))


@app.get("/update/<int:todo_id>")
def update(todo_id):
    db = get_db_connection()
    
    state = db.execute("SELECT completed FROM ToDo_Users WHERE id = ?", (todo_id,)).fetchone()[0]
    state = not state
    
    db.execute("UPDATE ToDo_Users SET completed = ? WHERE id = ?", (state, todo_id))
    db.commit()
    db.close()

    return redirect(url_for("home"))


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    
    db = get_db_connection()
    db.execute("DELETE FROM ToDo_Users WHERE id = ?", (todo_id))
    db.commit()
    db.close()

    return redirect(url_for("home"))


@app.route("/weather", methods=("POST", "GET"))
def weather():
    user_id = session.get('user_id')
    if user_id is None:
        flash("Пожалуйста, войдите в систему")
        return redirect(url_for("form_login"))
    
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather_data(city)

        if not weather_data:
            return redirect(url_for("error"))

        city = weather_data["name"]
        temperature = int(weather_data["main"]["temp"])
        icon = weather_data["weather"][0]["icon"]

        return render_template(
            "weather.html", city=city, temperature=temperature, icon=icon
        )

    return render_template("weather.html")


@app.route("/valuta", methods=("POST", "GET"))
def valuta():
    response = requests.get(url="https://api.exchangerate-api.com/v4/latest/USD").json()
    currencies = response.get("rates")

    if request.method == "GET":
        context = {"currencies": currencies}
        # print(context)

        return render_template("valuta.html", context=context)

    if request.method == "POST":
        from_amount = float(request.form.get("from-amount"))
        from_curr = request.form.get("from-curr")
        to_curr = request.form.get("to-curr")

        converted_amount = round(
            (currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2
        )
        print(converted_amount)

        context = {
            "from_curr": from_curr,
            "to_curr": to_curr,
            "from_amount": from_amount,
            "currencies": currencies,
            "converted_amount": converted_amount,
        }

        return render_template("index.html", context=context)


@app.route("/error")
def error():
    error_message = "Ошибка при запросе данных"
    return render_template("error.html", error_message=error_message)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/doc")
def doc():
    return render_template("document.html")
