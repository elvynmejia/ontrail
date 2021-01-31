from marshmallow import Schema, fields, validate, post_dump
from constants import STATES
from constants import DATETIME_FORMAT


class LeadEntity(Schema):
    __envelope__ = {
        "single": "lead",
        "many": "leads",
    }

    __internal__ = False

    id = fields.Int(dump_only=True)
    public_id = fields.Str(dump_only=True)
    company_name = fields.Str(required=True)
    role = fields.Str(required=True)
    contacts = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    status = fields.Str(
        required=False, validate=validate.OneOf(STATES.values()), allow_none=True
    )

    reference = fields.Str(required=False)
    current_stage_id = fields.Int(required=False)

    leads = fields.List(fields.Nested(lambda: "StageEntity"), dump_only=True)

    created_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)
    updated_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)

    @post_dump
    def post_dump_rocess(self, data, many, **kwargs):
        default_data = {
            "id": data["id"],
            "company_name": data["company_name"],
            "role": data["role"],
            "contacts": data["description"],
            "description": data["description"],
            "status": data["status"],
            "reference": data["reference"],
            "current_stage_id": data["current_stage_id"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
        }

        if self.__internal__:
            return {**default_data, "public_id": data["public_id"]}
        else:
            if data["current_stage_id"]:
                from repos.stage import (
                    StageRepo,
                )  # to avoid circular deps error for now

                current_stage_id_to_public_id = StageRepo.find(
                    id=data["current_stage_id"]
                )

                return {
                    **default_data,
                    "id": data["public_id"],
                    "current_stage_id": current_stage_id_to_public_id.public_id,
                }

            return {
                **default_data,
                "id": data["public_id"],
            }

    @classmethod
    def as_json(self, data, internal=False):

        self.__internal__ = internal

        if isinstance(data, list):
            key = self.__envelope__["many"]
            return {key: list(map(lambda entry: self().dump(entry), data))}
        else:
            key = self.__envelope__["single"]
            return {key: self().dump(data)}
