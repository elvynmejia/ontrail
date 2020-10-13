from marshmallow import Schema, fields, validate
from models.lead import STATES


class LeadEntity(Schema):
    id = fields.Int(dump_only=True)
    company_name = fields.Str(required=True)
    position = fields.Str()
    contacts = fields.Str(required=True)
    description = fields.Str()
    status = fields.Str(required=True, validate=validate.OneOf(STATES.values()))

    leads = fields.List(
        fields.Nested(lambda: "StageEntity"), dump_only=True
    )  # circular dep

    def as_json(self, record):
        return self.dump(record)
