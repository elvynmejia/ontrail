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

        try:
            lead = self.lead()
        except (UnprocessableEntity, NotFound) as error:
            return error.as_json(), error.http_code
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
                "lead_id": lead.id,
                "state": json_data.get("state"),
                "start_at": start_at,
                "end_at": end_at,
            }

            data = StageEntity().load(params)

        except ValidationError as err:
            # this should be abstracted to an error handler
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code

        stage = StageRepo.create(**{**data, "lead_id": lead.id})
        return(StageEntity.as_json(stage), 201)

    def lead(self):
        try:
            lead_id = request.get_json()["lead_id"]
        except KeyError:
            raise UnprocessableEntity(errors=[{"lead_id": ["Field may not be null."]}])

        try:
            return LeadRepo.find(public_id=lead_id)
        except (RecordNotFound, KeyError) as err:
            raise NotFound(
                message="Cannot find Lead by given lead_id {}".format(lead_id)
            )

    def start_at(self):

        json_data = request.get_json()

        if json_data.get("start_at"):
            try:
                return datetime.strptime(
                    json_data.get("start_at"), DATETIME_FORMAT
                ).strftime(DATETIME_FORMAT)
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
                return datetime.strptime(
                    json_data.get("end_at"), DATETIME_FORMAT
                ).strftime(DATETIME_FORMAT)
            except (ValueError, TypeError):
                raise UnprocessableEntity(
                    message=datetime_validation_error_message.format(
                        "end_at", DATETIME_FORMAT, json_data.get("end_at")
                    )
                )
