from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity


class List(MethodView):
    def get(self):
        leads = LeadRepo.find_all()

        # find a way to call as_json automatically before the response
        # is returrned to the client
        return ({"leads": LeadEntity(many=True).as_json(leads)}, 200)
