from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class Show(MethodView):
    def get(self, id):
        lead = LeadRepo.find(id=id)
        return {"lead": LeadEntity().as_json(lead)}, 200
