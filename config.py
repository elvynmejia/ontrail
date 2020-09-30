from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base config."""
    SECRET_KEY = environ['SECRET_KEY']
    DATABASE_URI = environ['DATABASE_URI']

    # set defaults
    FLASK_APP = environ.get('FLASK_APP', 'app.py')
    DEBUG = environ.get('DEBUG', False)
    TESTING = environ.get('TESTING', False)
    FLASK_ENV = environ.get('FLASK_ENV', 'production')

