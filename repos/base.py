from sqlalchemy import desc
from db_config import db
from .error import RecordNotFound
from datetime import datetime


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
        else:
            raise Exception

    @classmethod
    def find(cls, **kwargs):
        record = cls.model().query.filter_by(**kwargs).first()

        # should raise an error if no record
        if record:
            return record
        raise RecordNotFound()

    @classmethod
    def find_all(cls, **kwargs):
        records = cls.model().query.filter_by(**kwargs).all()
        return records

    @classmethod
    def update(cls, id, **kwargs):
        result = (
            db.session.query(cls.model())
            .filter_by(id=id)
            .update(
                kwargs,
            )
        )

        # rescue exception here
        db.session.commit()
        return cls.find(id=id)

    @classmethod
    def delete(cls, id):
        result = (
            db.session.query(cls.model())
            .filter_by(id=id)
            .update(
                {"disabled_at": datetime.now()},
            )
        )

        # rescue exception here
        db.session.commit()
        return cls.find(id=id)

    @classmethod
    def paginate(cls, page=1, per_page=20, **kwargs):
        query = (
            cls.model()
            .query.filter_by(**kwargs)
            .order_by(desc(cls.model().id))
            .paginate(page, per_page)
        )
        return query.items, query.total  # probably expensice to run total
