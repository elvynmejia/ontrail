import os
import config
import models
from seed import seed_bp

from db_config import db, migrate
from flask import Flask, jsonify, request
from repos import LeadRepo
from entities import LeadEntity

import pdb

from marshmallow import ValidationError


def health_check_ok():
    return "Ok"


def health_check_boom():
    raise SystemError  # change to internal error


def get_leads():
    leads = LeadRepo.find_all()
    # find a way to call as_json automatically before the response
    # is returrned to the client
    return {"leads": LeadEntity(many=True).as_json(leads)}, 200


def create_lead():
    json_data = request.get_json()

    try:
        data = LeadEntity().load(json_data)
    except ValidationError as err:
        return {"errors": [err.messages], "message": "Unprocessable Entity", "code": "UNPROCESSABLE_ENTITY"}, 422

    lead = LeadRepo.create(**data)
    return {"lead": LeadEntity().as_json(lead)}, 201


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(seed_bp)

    # health API
    app.add_url_rule("/health/ok", view_func=health_check_ok, methods=["GET"])
    app.add_url_rule("/health/boom", view_func=health_check_boom, methods=["GET"])

    # leads API
    app.add_url_rule("/v1/leads", view_func=get_leads, methods=["GET"])
    app.add_url_rule("/v1/leads", view_func=create_lead, methods=["POST"])

    return app
