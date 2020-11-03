from marshmallow import Schema, fields, validate
from constants import STATES


class LeadEntity(Schema):
    id = fields.Int(dump_only=True)
    company_name = fields.Str(required=True)
    position = fields.Str(allow_none=True)
    contacts = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    status = fields.Str(
        required=False, validate=validate.OneOf(STATES.values()), allow_none=True
    )

    leads = fields.List(
        fields.Nested(lambda: "StageEntity"), dump_only=True
    )

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def as_json(self, record):
        return self.dump(record)
