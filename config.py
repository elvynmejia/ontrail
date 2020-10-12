from os import environ, path
from dotenv import load_dotenv

load_dotenv()

basedir = path.abspath(path.dirname(__file__))


class Dev:
    """Base config."""

    SECRET_KEY = environ["SECRET_KEY"]

    # set defaults
    FLASK_APP = environ.get("FLASK_APP", "app.py")
    DEBUG = environ.get("DEBUG", False)
    TESTING = environ.get("TESTING", False)
    FLASK_ENV = environ.get("FLASK_ENV", "production")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or "sqlite:///" + path.join(
        basedir, "app.db"
    )

class Test:
    """Base config."""

    SECRET_KEY = environ["SECRET_KEY"]

    # set defaults
    FLASK_APP = environ.get("FLASK_APP", "app.py")
    DEBUG = environ.get("DEBUG", False)
    TESTING = environ.get("TESTING", False)
    FLASK_ENV = environ.get("FLASK_ENV", "test")
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL") or "sqlite:///" + path.join(
        basedir, "app_test.db"
    )
    TESTING = True