from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from repos.error import RecordNotFound
from actions.error import NotFound, UnprocessableEntity
from entities import StageEntity


class Update(MethodView):
    def patch(self, id):
        try:
            stage = StageRepo.find(id=id)
        except RecordNotFound:
            error = NotFound(message="Stage with id {} not found".format(id))

        json_data = request.get_json()

        try:
            params = {
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                # "lead_id": lead.id,
                "state": "phone_screen",
            }

            data = StageEntity(partial=True).load(params)

            updated_stage = StageRepo.update(id=id, **data)
            return ({"stage": updated_stage.as_json()}, 200)
        except ValidationError as err:
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code
