from marshmallow import fields, validate, post_dump
from .base import BaseEntity
from constants import STAGE_STATUSES
from constants import DATETIME_FORMAT


class StageEntity(BaseEntity):
    __envelope__ = {
        "single": "stage",
        "many": "stages",
    }

    __internal__ = False

    id = fields.Int(dump_only=True)
    public_id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    links = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    lead_id = fields.Int(required=True)
    state = fields.Str(required=False, validate=validate.OneOf(STAGE_STATUSES.values()))
    reference = fields.Str(required=False)

    start_at = fields.DateTime(required=False, allow_none=True, format=DATETIME_FORMAT)
    end_at = fields.DateTime(required=False, allow_none=True, format=DATETIME_FORMAT)
    created_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)
    updated_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)
    disabled_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)

    @post_dump
    def post_dump_rocess(self, data, many, **kwargs):
        default_data = {
            "id": data["id"],
            "title": data["title"],
            "links": data["links"],
            "description": data["description"],
            "notes": data["notes"],
            "lead_id": data["lead_id"],
            "state": data["state"],
            "reference": data["reference"],
            "start_at": data["start_at"],
            "end_at": data["end_at"],
            "created_at": data["created_at"],
            "updated_at": data["updated_at"],
            "disabled_at": data["disabled_at"],
        }

        if self.__internal__:
            return {**default_data, "public_id": data["public_id"]}
        else:

            from repos import (
                LeadRepo,
            )  # to avoid circular deps error for now

            return {
                **default_data,
                "id": data["public_id"],
                "lead_id": LeadRepo.find(id=data["lead_id"]).public_id,
            }
