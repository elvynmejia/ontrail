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

        try:
            start_at = self.start_at()
            end_at = self.end_at()
        except UnprocessableEntity as error:
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

    def start_at(self):

        json_data = request.get_json()

        if json_data.get("start_at"):
            try:
                parsed_start_at = datetime.strptime(
                    json_data.get("start_at"), DATETIME_FORMAT
                )

                if parsed_start_at:
                    return parsed_start_at.strftime(DATETIME_FORMAT)

            except (ValueError, TypeError):
                raise UnprocessableEntity(
                    message=datetime_validation_error_message.format(
                        "start_at", DATETIME_FORMAT, json_data.get("start_at")
                    )
                )

    def end_at(self):
        json_data = request.get_json()

        if json_data.get("end_at"):
            try:
                parsed_end_at = datetime.strptime(
                    json_data.get("end_at"), DATETIME_FORMAT
                )

                if parsed_end_at:
                    return parsed_end_at.strftime(DATETIME_FORMAT)

            except (ValueError, TypeError):
                raise UnprocessableEntity(
                    message=datetime_validation_error_message.format(
                        "end_at", DATETIME_FORMAT, json_data.get("end_at")
                    )
                )
