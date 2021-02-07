from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo, StageRepo
from repos.error import RecordNotFound
from entities import LeadEntity
from actions.error import NotFound, UnprocessableEntity
from decorators import validate_public_id


class Update(MethodView):

    decorators = [validate_public_id]

    def current_stage(self):
        current_stage_id = request.get_json().get("current_stage_id")
        if current_stage_id:
            try:
                return StageRepo.find(public_id=current_stage_id)
            except RecordNotFound:
                raise NotFound(
                    message="Current Stage with current_stage_id {} not found".format(
                        current_stage_id
                    )
                )

    def patch(self, id):
        try:
            lead = LeadRepo.find(public_id=id)
        except RecordNotFound as err:
            error = NotFound(message="Lead with id {} not found".format(id))
            return (error.as_json(), error.http_code)

        json_data = request.get_json()

        params = {
            "company_name": json_data.get("company_name"),
            "role": json_data.get("role"),
            "contacts": json_data.get("contacts"),
            "description": json_data.get("description"),
            "status": json_data.get("status"),
            "reference": json_data.get("reference"),
        }

        if json_data.get("current_stage_id"):
            try:
                current_stage = self.current_stage()
                params = {**params, "current_stage_id": current_stage.id}
            except NotFound as error:
                return error.as_json(), error.http_code

        try:
            data = LeadEntity(partial=True, load_only=["id"]).load(params)

            updated_lead = LeadRepo.update(id=lead.id, **data)

            return ({"lead": updated_lead.as_json()}, 200)
        except ValidationError as err:
            error = UnprocessableEntity(errors=[err.messages])
            return error.as_json(), error.http_code
