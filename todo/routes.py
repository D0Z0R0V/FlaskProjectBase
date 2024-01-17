import requests
from flask import Flask, render_template, request, url_for, redirect
#from todo.form import SiteForm

from todo.models import ToDo, db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    return app


app = create_app()


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


@app.get("/")
def home():
    todo_list = ToDo.query.all()
    return render_template("index.html", todo_list=todo_list, title="Главная страница")


@app.post("/add")
def add():
    title = request.form.get("title")
    new_todo = ToDo(title=title, is_complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/update/<int:todo_id>")
def update(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    todo.is_complete = not todo.is_complete
    db.session.commit()
    return redirect(url_for("home"))


@app.get("/delete/<int:todo_id>")
def delete(todo_id):
    todo = ToDo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/weather", methods=("POST", "GET"))
def weather():
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


@app.route("/login", methods=["GET", "POST"])
def login():
    
    return render_template("forma.html")


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
