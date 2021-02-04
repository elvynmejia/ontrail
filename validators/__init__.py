from marshmallow import Schema, fields, validate, post_load


class IdValidator(Schema):
    id = fields.Int(required=True)


class PublicIdValidator(Schema):
    id = fields.Str(required=True, allow_none=False)
