from marshmallow import Schema, fields, validate
# from models import STAGE_STATUSES
from models.lead import STATES

class StageEntity(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    links = fields.Str()
    description = fields.Str()
    notes = fields.Str()
    lead_id = fields.Int(required=True)
    state = fields.Str(
       required=False, validate=validate.OneOf(STATES.values())
    )

    def as_json(self, record):
        return self.dump(record)
