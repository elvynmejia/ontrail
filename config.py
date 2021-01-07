from os import environ, path
from dotenv import load_dotenv

load_dotenv()

basedir = path.abspath(path.dirname(__file__))


class BaseConfig:
    """Base config."""

    SECRET_KEY = environ["SECRET_KEY"]
    FLASK_APP = environ.get("FLASK_APP", "app.py")
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")


class Dev(BaseConfig):
    """Dev config."""

    DEBUG = True
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql" + "://root:root@localhost:3306/ontrail_dev"
    )


class Test(BaseConfig):
    """Test config."""

    DEBUG = True
    TESTING = True
    FLASK_ENV = "test"
    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql" + "://root:root@localhost:3306/ontrail_test"
    )
    TESTING = True
