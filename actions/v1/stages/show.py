from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class Show(MethodView):
    def get(self, id):
        stage = StageRepo.find(id=id)
        return {"stage": StageEntity().as_json(stage)}, 200
