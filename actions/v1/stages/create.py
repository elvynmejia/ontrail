from flask.views import MethodView, request
from marshmallow import ValidationError

from repos import StageRepo
from entities import StageEntity


class Create(MethodView):
    def post(self):
        json_data = request.get_json()

        try:
            data = StageEntity().load(json_data)
        except ValidationError as err:
            return (
                {
                    "errors": [err.messages],
                    "message": "Unprocessable Entity",
                    "code": "UNPROCESSABLE_ENTITY",
                },
                422,
            )

        stage = StageRepo.create(**data)
        return {"stage": StageEntity().as_json(stage)}, 201
