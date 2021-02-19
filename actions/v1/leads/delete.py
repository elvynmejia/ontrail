from flask.views import MethodView, request
from marshmallow import ValidationError
from functools import wraps

from repos import LeadRepo
from entities import LeadEntity
from repos.error import RecordNotFound
from actions.error import NotFound
from decorators import validate_public_id


class Delete(MethodView):

    decorators = [validate_public_id]

    def delete(self, id):
        try:
            lead = LeadRepo.find(public_id=id)
            LeadRepo.delete(id=lead.id)

            return ("", 204)  # return empty body
        except RecordNotFound as err:
            error = NotFound(message="Lead with id {} not found".format(id))
            return (error.as_json(), error.http_code)
