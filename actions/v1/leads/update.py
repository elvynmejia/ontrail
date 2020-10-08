from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class Update(MethodView):
    def patch(self, id):
        json_data = request.get_json()

        try:
            data = LeadEntity(partial=True).load(json_data)
            updated_lead = LeadRepo.update(id=id, **data)
            return ({"lead": LeadEntity().as_json(updated_lead)}, 200)
        except ValidationError as err:
            return (
                {
                    "errors": [err.messages],
                    "message": "Unprocessable Entity",
                    "code": "UNPROCESSABLE_ENTITY",
                },
                422,
            )
