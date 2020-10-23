from marshmallow import Schema, fields, validate
from constants import STATES


class StageEntity(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    links = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    lead_id = fields.Int(required=True)
    state = fields.Str(required=False, validate=validate.OneOf(STATES.values()))
    start_at = fields.DateTime(required=True)
    end_at = fields.DateTime(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    def as_json(self, record):
        return self.dump(record)
