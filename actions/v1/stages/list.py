from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class List(MethodView):
    def get(self):
        stages = StageRepo.find_all()

        # find a way to call as_json automatically before the response
        # is returrned to the client
        return ({"stages": StageEntity(many=True).as_json(stages)}, 200)
