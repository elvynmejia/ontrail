from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo, LeadRepo
from entities import StageEntity
from repos.error import RecordNotFound
from actions.error import NotFound


class List(MethodView):
    def get(self):
        lead_id = request.args.get("lead_id")

        if lead_id:
            try:
                lead = LeadRepo.find(public_id=lead_id)
                result, total = StageRepo.paginate(**{"lead_id": lead.id})
            except RecordNotFound:
                error = NotFound(
                    message="Cannot filter stages by given lead_id {}".format(lead_1)
                )
                return error.as_json(), error.http_code
        else:
            result, total = StageRepo.paginate()

        # find a way to call as_json automatically before the response
        # is returrned to the client
        stages = list(map(lambda stage: stage.as_json(), result))
        return ({"stages": stages}, 200)
