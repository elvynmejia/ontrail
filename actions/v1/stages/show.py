from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from repos.error import RecordNotFound
from actions.error import NotFound
from entities import StageEntity
from decorators import validate_public_id


class Show(MethodView):

    decorators = [validate_public_id]

    def get(self, id):
        try:
            stage = StageRepo.find(public_id=id)
            return (StageEntity.as_json(stage), 200)
        except RecordNotFound:
            error = NotFound(message="Stage with id {} not found".format(id))
            return (error.as_json(), error.http_code)
