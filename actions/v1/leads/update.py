from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from repos.error import RecordNotFound
from entities import LeadEntity
from actions.error import NotFound, UnprocessableEntity


class Update(MethodView):
    def patch(self, id):
        try:
            lead = LeadRepo.find(id=id)
        except RecordNotFound as err:
            error = NotFound(message="Lead with id {} not found".format(id))
            return (error.as_json(), error.http_code)

        json_data = request.get_json()

        try:
            params = {
                "company_name": json_data.get("company_name"),
                "position": json_data.get("position"),
                "contacts": json_data.get("contacts"),
                "description": json_data.get("description"),
                "status": json_data.get("status"),
            }

            data = LeadEntity(partial=True, load_only=["id"]).load(params)

            updated_lead = LeadRepo.update(id=lead.id, **data)

            return ({"lead": updated_lead.as_json()}, 200)
        except ValidationError as err:
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code
