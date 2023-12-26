from todo.routes import app, db
from todo.config import Config

app.config.from_object(Config)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
