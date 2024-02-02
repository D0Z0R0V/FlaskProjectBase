import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "the secret key"
    SESSION_TYPE = 'filesystem' # тип хранилища сессий
    SESSION_PERMANENT = False # время жизни сессии