from os import environ
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    DEBUG = environ.get('DEBUG')
    TESTING = environ.get('TESTING')
    DATABASE_URI = environ.get('DATABASE_URI')

