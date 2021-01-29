from marshmallow import Schema, fields, validate
from constants import STATES
from constants import DATETIME_FORMAT


class LeadEntity(Schema):
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
