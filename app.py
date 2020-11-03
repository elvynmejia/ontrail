from os import environ
from flask import Flask, jsonify, request
from dotenv import load_dotenv

import config
import models

from seed import seed_bp
from routes.v1 import routes_bp

from db_config import db, migrate


load_dotenv()


def health_check_ok():
    return "Ok"


def health_check_boom():
    raise SystemError  # change to internal error


def create_app(testing=False):
    app = Flask(__name__)

    env = environ["FLASK_ENV"]

    if env == "production":
        app.config.from_object("config.BaseConfig")
    elif env == "development":
        app.config.from_object("config.Dev")

    if testing:
        app.config.from_object("config.Test")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(seed_bp)
    app.register_blueprint(routes_bp)

    # health API
    app.add_url_rule("/health/ok", view_func=health_check_ok, methods=["GET"])
    app.add_url_rule("/health/boom", view_func=health_check_boom, methods=["GET"])

    return app
