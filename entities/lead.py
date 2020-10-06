from marshmallow import Schema, fields


class LeadEntity(Schema):
    name = fields.Str()
    contacts = fields.Str()
    # description = fields.Text()

    def as_json(self, record):
        return self.dump(record)
