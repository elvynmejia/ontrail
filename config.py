from os import environ, path
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    """Base config."""

    SECRET_KEY = environ["SECRET_KEY"]
    FLASK_APP = environ.get("FLASK_APP", "app.py")
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Dev(BaseConfig):
    """Dev config."""

    DEBUG = True
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql" + "://root:root@localhost:3306/ontrail_dev"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class Test(BaseConfig):
    """Test config."""

    DEBUG = True
    TESTING = True
    FLASK_ENV = "test"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql" + "://root:root@localhost:3306/ontrail_test"
    )
    TESTING = True
