from flask import jsonify
from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class Create(MethodView):
    def post(self):
        json_data = request.get_json()
        try:
            kwargs = {
                "company_name": json_data["company_name"],
                "position": json_data["position"],
                "contacts": json_data["contacts"],
                "description": json_data.get("description"),
                "status": json_data.get("status"),
            }

            data = LeadEntity().load(kwargs)

        except ValidationError as err:
            return (
                {
                    "errors": [err.messages],
                    "message": "Unprocessable Entity",
                    "code": "UNPROCESSABLE_ENTITY",
                },
                422,
            )

        lead = LeadRepo.create(**data)
        return ({"lead": lead.as_json()}, 201)
