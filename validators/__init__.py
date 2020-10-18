from marshmallow import Schema, fields, validate, post_load


class IdValidator(Schema):
    id = fields.Int(required=True, error_messages={"required": "id missing."})