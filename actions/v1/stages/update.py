from flask.views import MethodView, request
from marshmallow import ValidationError
from datetime import datetime

from repos import StageRepo
from repos.error import RecordNotFound
from actions.error import NotFound, UnprocessableEntity
from entities import StageEntity
from decorators import validate_id
from constants import DATETIME_FORMAT

datetime_validation_error_message = (
    "Invalid {} datetime format." "Example datetime format allowed {}. Given {}"
)


class Update(MethodView):

    decorators = [validate_id]

    def patch(self, id):
        try:
            stage = StageRepo.find(id=id)
        except RecordNotFound:
            error = NotFound(message="Stage with id {} not found".format(id))
            return error.as_json(), error.http_code

        json_data = request.get_json()

        start_at = None
        end_at = None

        if json_data.get("start_at"):
            try:
                start_at = datetime.strptime(
                    json_data.get("start_at"), DATETIME_FORMAT
                ).strftime(DATETIME_FORMAT)
            except (ValueError, TypeError):
                error = UnprocessableEntity(
                    message=datetime_validation_error_message.format(
                        "start_at", DATETIME_FORMAT, json_data.get("start_at")
                    )
                )
                return error.as_json(), error.http_code

        if json_data.get("end_at"):
            try:
                end_at = datetime.strptime(
                    json_data.get("end_at"), DATETIME_FORMAT
                ).strftime(DATETIME_FORMAT)
            except (ValueError, TypeError):
                error = UnprocessableEntity(
                    message=datetime_validation_error_message(
                        "end_at", DATETIME_FORMAT, json_data.get("end_at")
                    )
                )
                return error.as_json(), error.http_code

        try:
            params = {
                "title": json_data.get("title"),
                "links": json_data.get("links"),
                "description": json_data.get("description"),
                "notes": json_data.get("notes"),
                "lead_id": json_data.get("lead_id"),
                "state": json_data.get("state"),
                "start_at": start_at,
                "end_at": end_at,
            }

            data = StageEntity().load(params)

            updated_stage = StageRepo.update(id=id, **data)
            return ({"stage": updated_stage.as_json()}, 200)
        except ValidationError as err:
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code
