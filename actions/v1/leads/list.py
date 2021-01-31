from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class List(MethodView):
    def get(self):
        page = 1
        per_page = 10
        result, total = LeadRepo.paginate(page, per_page)
        data = LeadEntity.as_json(result)
        return (data, 200)
