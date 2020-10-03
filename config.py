from os import environ
from dotenv import load_dotenv

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    """Base config."""
    SECRET_KEY = environ['SECRET_KEY']
    
    # set defaults
    FLASK_APP = environ.get('FLASK_APP', 'app.py')
    DEBUG = environ.get('DEBUG', False)
    TESTING = environ.get('TESTING', False)
    FLASK_ENV = environ.get('FLASK_ENV', 'production')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

