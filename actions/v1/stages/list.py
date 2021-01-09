from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class List(MethodView):
    def get(self):
        lead_id = request.args.get("lead_id")
        # import pdb; pdb.set_trace()
        result, total = StageRepo.paginate(**{"lead_id": lead_id})
        if lead_id:
            result, total = StageRepo.paginate(**{"lead_id": lead_id})
        else:
            result, total = StageRepo.paginate()

        # find a way to call as_json automatically before the response
        # is returrned to the client
        stages = list(map(lambda stage: stage.as_json(), result))
        return ({"stages": stages}, 200)
