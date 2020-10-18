from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class List(MethodView):
    def get(self):
        result, total = StageRepo.paginate()

        # find a way to call as_json automatically before the response
        # is returrned to the client
        stages = list(map(lambda stage: stage.as_json(), result))
        return ({"stages": stages}, 200)
