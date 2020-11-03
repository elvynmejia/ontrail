from flask import jsonify
from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity
from actions.error import UnprocessableEntity


class Create(MethodView):
    def post(self):
        json_data = request.get_json()
        try:
            params = {
                "company_name": json_data.get("company_name"),
                "position": json_data.get("position"),
                "contacts": json_data.get("contacts"),
                "description": json_data.get("description"),
                "status": json_data.get("status"),
            }

            data = LeadEntity().load(params)

            lead = LeadRepo.create(**data)
            return ({"lead": lead.as_json()}, 201)
        except ValidationError as err:
            # this should be abstracted to an error handler
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code
