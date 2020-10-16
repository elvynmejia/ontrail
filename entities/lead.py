from marshmallow import Schema, fields, validate, post_load
from constants import STATES


class LeadEntity(Schema):
    id = fields.Int(dump_only=True)
    company_name = fields.Str(required=True)
    position = fields.Str(allow_none=True)
    contacts = fields.Str(required=True)
    description = fields.Str(allow_none=True)
    status = fields.Str(required=False, validate=validate.OneOf(STATES.values()), allow_none=True)

    leads = fields.List(
        fields.Nested(lambda: "StageEntity"), dump_only=True
    )  # circular dep

    # @post_load
    # def make_user(self, data, **kwargs):
    #     return Lead(**data)

    def as_json(self, record):
        return self.dump(record)
