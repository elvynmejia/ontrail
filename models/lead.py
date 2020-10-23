from datetime import datetime
from entities.lead import LeadEntity
from db_config import db
from constants import STATES


class Lead(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    # company
    company_name = db.Column(db.String, nullable=False)

    position = db.Column(db.String, nullable=True)

    contacts = db.Column(db.String, nullable=False)

    description = db.Column(db.Text, nullable=True)

    status = db.Column(db.String, nullable=False, default=STATES.get("unscheduled"))

    # relationships
    stages = db.relationship("Stage", backref="lead", lazy="dynamic")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    updated_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

    def as_json(self):
        return LeadEntity().dump(self)

    def __repr__(self):
        return (
            "Lead(id = {}, company_name = {}, position = {} contacts = {}, description = {} "
            "status = {}, created_at = {}, updated_at = {})"
            "".format(
                repr(self.id),
                repr(self.company_name),
                repr(self.position),
                repr(self.contacts),
                repr(self.description),
                repr(self.status),
                repr(self.created_at),
                repr(self.updated_at),
            )
        )
