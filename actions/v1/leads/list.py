from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class List(MethodView):
    def get(self):
        result, total = LeadRepo.paginate()
        data = LeadEntity.as_json(result)
        return (data, 200)
