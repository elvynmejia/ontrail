from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class Update(MethodView):
    def patch(self, id):
        json_data = request.get_json()

        try:
            data = StageEntity(partial=True).load(json_data)
            updated_stage = StageRepo.update(id=id, **data)
            return ({"stage": StageEntity().as_json(updated_stage)}, 200)
        except ValidationError as err:
            return (
                {
                    "errors": [err.messages],
                    "message": "Unprocessable Entity",
                    "code": "UNPROCESSABLE_ENTITY",
                },
                422,
            )
