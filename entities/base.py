from marshmallow import Schema, post_dump


class BaseEntity(Schema):
    @classmethod
    def as_json(self, data, internal=False):

        self.__internal__ = internal

        if isinstance(data, list):
            key = self.__envelope__["many"]
            return {key: list(map(lambda entry: self().dump(entry), data))}
        else:
            key = self.__envelope__["single"]
            return {key: self().dump(data)}

    @post_dump
    def post_dump_rocess(self, data, many, **kwargs):
        raise NotImplementedError
