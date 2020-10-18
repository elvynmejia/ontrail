from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from repos.error import RecordNotFound
from actions.error import NotFound
from entities import StageEntity
from decorators import validate_id


class Show(MethodView):

    decorators = [validate_id]

    def get(self, id):
        try:
            stage = StageRepo.find(id=id)
            return ({'stage': stage.as_json()}, 200)
        except RecordNotFound:
            error = \
                NotFound(message='Stage with id {} not found'.format(id))
            return (error.as_json(), error.http_code)