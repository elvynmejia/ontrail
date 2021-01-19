from marshmallow import Schema, fields, validate
from constants import STATES
from constants import DATETIME_FORMAT


class StageEntity(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    links = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    lead_id = fields.Int(required=True)
    state = fields.Str(required=False, validate=validate.OneOf(STATES.values()))
    reference = fields.Str(required=False)

    start_at = fields.DateTime(required=False, allow_none=True, format=DATETIME_FORMAT)
    end_at = fields.DateTime(required=False, allow_none=True, format=DATETIME_FORMAT)
    created_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)
    updated_at = fields.DateTime(dump_only=True, format=DATETIME_FORMAT)
