from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import LeadRepo
from entities import LeadEntity
from constants import LEAD_STATUSES
from actions.error import UnprocessableEntity


class List(MethodView):
    def valiate_status(self):
        try:
            LEAD_STATUSES[request.args.get("status")]
        except KeyError:
            raise UnprocessableEntity(
                message="Invalid status. Allowed statuses {}".format(
                    LEAD_STATUSES.keys()
                )
            )

    def get(self):
        try:
            if request.args.get("status"):
                self.valiate_status()
                status = request.args.get("status")
                result, total = LeadRepo.paginate(**{"status": status})
                return (LeadEntity.as_json(result), 200)
        except UnprocessableEntity as error:
            return error.as_json(), error.http_code

        result, total = LeadRepo.paginate()

        return (LeadEntity.as_json(result), 200)
