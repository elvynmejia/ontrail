from inflection import underscore
from db_config import db
from .error import RecordNotFound


class BaseRepo:
    @classmethod
    def model(cls):
        raise NotImplementedError

    @classmethod
    def entity(cls):
        raise NotImplementedError

    @classmethod
    def create(cls, **kwargs):
        record = cls.model()(**kwargs)
        db.session.add(record)
        db.session.commit()

        if record:
            return record

    @classmethod
    def find(cls, **kwargs):
        record = cls.model().query.filter_by(**kwargs).first()

        # should raise an error if no record
        if record:
            return record
        raise RecordNotFound

    @classmethod
    def find_all(cls, **kwargs):
        records = cls.model().query.filter_by(**kwargs).all()
        return records

    @classmethod
    def update(cls, id, **kwargs):
        # update returns 1 or 0
        record = cls.model().query.filter_by(id=id).update(kwargs)

        # should raise an error if no record
        if record:
            return cls.find(id=id)
