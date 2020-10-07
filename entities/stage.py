from marshmallow import Schema, fields, validate
from models import STAGE_STATUSES


class StageEntity(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    links = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    lead_id = fields.Int(dump_only=True)
    status = fields.Str(
        required=False, validate=validate.OneOf(STAGE_STATUSES.values())
    )

    def as_json(self, record):
        return self.dump(record)
