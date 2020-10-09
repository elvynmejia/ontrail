import os
import config
import models

from seed import seed_bp
from routes.v1 import routes_bp

from db_config import db, migrate
from flask import Flask, jsonify, request

import pdb


def health_check_ok():
    return "Ok"


def health_check_boom():
    raise SystemError  # change to internal error


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(seed_bp)
    app.register_blueprint(routes_bp)

    # health API
    app.add_url_rule("/health/ok", view_func=health_check_ok, methods=["GET"])
    app.add_url_rule("/health/boom", view_func=health_check_boom, methods=["GET"])

    return app
