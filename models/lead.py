from datetime import datetime
from entities.lead import LeadEntity
from db_config import db
from constants import STATES
from .util import generate_public_id


class Lead(db.Model):
    __tablename__ = "leads"
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    public_id = db.Column(
        db.String(32),
        nullable=True,
        default=lambda context: generate_public_id(context, Lead),
        unique=True,
    )

    company_name = db.Column(db.String(100), nullable=False)

    position = db.Column(db.String(100), nullable=False)

    contacts = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text(400), nullable=True)

    status = db.Column(
        db.String(100), nullable=False, default=STATES.get("unscheduled")
    )

    reference = db.Column(db.String(100), nullable=True)

    current_stage_id = db.Column(
        db.Integer,
        nullable=True,
    )

    # relationships
    # stages = db.relationship("Stage", backref="lead", lazy="dynamic")

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )

    def as_json(self):
        return LeadEntity().dump(self)

    def __repr__(self):
        return (
            "Lead(id = {}, public_id = {}, company_name = {}, position = {} contacts = {}, description = {} "
            "status = {}, reference = {}, current_stage_id = {}, created_at = {}, updated_at = {})"
            "".format(
                repr(self.id),
                repr(self.public_id),
                repr(self.company_name),
                repr(self.position),
                repr(self.contacts),
                repr(self.description),
                repr(self.status),
                repr(self.reference),
                repr(self.current_stage_id),
                repr(self.created_at),
                repr(self.updated_at),
            )
        )
