Устанавливаем и активируем виртуальное окружение

python3 -m venv venv
. venv/bin/activate
Активируем git

git init
Создаем файлы и папки в проекте

Устанавливаем flask и ORM SQLAlchemy

pip install Flask Flask-SQLAlchemy
Создаем файл с зависимостями проекта

pip freeze > requirements.txt
Устанавливаем переменные окружения

для bash

export FLASK_APP=app.py
export FLASK_ENV=development
для cmd

set FLASK_APP=app.py
set FLASK_ENV=development
Запускаем приложение

flask run

Ссылка на оригинал
https://www.youtube.com/watch?v=3vfum74ggHE
