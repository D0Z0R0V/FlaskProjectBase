import os

from dotenv import load_dotenv

load_dotenv()

# /// = relative path, //// = absolute path
FLASK_APP = os.getenv('FLASK_APP')
FLASK_ENV = os.getenv('FLASK_ENV')
SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
