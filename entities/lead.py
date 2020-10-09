from marshmallow import Schema, fields, validate
from models import LEAD_STATUSES


class LeadEntity(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    contacts = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True, validate=validate.OneOf(LEAD_STATUSES.values()))

    leads = fields.List(
        fields.Nested(lambda: "StageEntity"), dump_only=True
    )  # circular dep

    def as_json(self, record):
        return self.dump(record)
