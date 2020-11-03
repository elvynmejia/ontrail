from flask.views import MethodView, request
from marshmallow import ValidationError
from functools import wraps

from repos import LeadRepo
from entities import LeadEntity
from repos.error import RecordNotFound
from actions.error import NotFound
from decorators import validate_id


class Show(MethodView):

    decorators = [validate_id]

    def get(self, id):
        try:
            lead = LeadRepo.find(id=id)
            return ({"lead": lead.as_json()}, 200)
        except RecordNotFound as err:
            error = NotFound(message="Lead with id {} not found".format(id))
            return (error.as_json(), error.http_code)
