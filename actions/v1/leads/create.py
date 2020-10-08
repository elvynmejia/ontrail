from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class Create(MethodView):
    def post(self):
        json_data = request.get_json()

        try:
            data = LeadEntity().load(json_data)
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
        return {"lead": LeadEntity().as_json(lead)}, 201
