from datetime import datetime
from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo, LeadRepo
from repos.error import RecordNotFound
from actions.error import UnprocessableEntity, NotFound
from entities import StageEntity
from constants import DATETIME_FORMAT

datetime_validation_error_message = (
    "Invalid {} datetime format." "Example datetime format allowed {}. Given {}"
)


class Create(MethodView):
    def post(self):
        json_data = request.get_json()

        start_at = self.start_at()
        end_at = self.end_at()

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

        except ValidationError as err:
            # this should be abstracted to an error handler
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code

        try:
            lead = LeadRepo.find(id=params["lead_id"])
        except RecordNotFound as err:
            error = NotFound(
                message="Cannot find Lead by given lead_id {}".format(params["lead_id"])
            )
            return error.as_json(), error.http_code

        stage = StageRepo.create(**{**data, "lead_id": lead.id})
        return {"stage": stage.as_json()}, 201

    def start_at(self):
        start_at = None

        json_data = request.get_json()

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

        return start_at

    def end_at(self):
        json_data = request.get_json()

        end_at = None

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

        return end_at
