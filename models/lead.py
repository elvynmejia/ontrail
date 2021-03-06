from datetime import datetime
from entities.lead import LeadEntity
from db_config import db
from constants import LEAD_STATUSES
from .util import generate_public_id, generate_url


class Lead(db.Model):
    __tablename__ = "leads"
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    public_id = db.Column(
        db.String(32),
        nullable=False,
        default=lambda context: generate_public_id(context, Lead, "lead"),
        unique=True,
    )

    company_name = db.Column(db.String(100), nullable=False)

    url = db.Column(db.String(100), nullable=False, default=generate_url)

    role = db.Column(db.String(100), nullable=False)

    contacts = db.Column(db.String(100), nullable=False)

    description = db.Column(db.Text(400), nullable=True)

    status = db.Column(
        db.String(100), nullable=False, default=LEAD_STATUSES.get("unscheduled")
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

    disabled_at = db.Column(db.DateTime, nullable=True)

    def as_json(self):
        return LeadEntity().dump(self)

    def __repr__(self):
        return (
            "Lead(id = {}, public_id = {}, company_name = {}, url = {}, role = {} contacts = {}, description = {} "
            "status = {}, reference = {}, current_stage_id = {}, created_at = {}, updated_at = {} "
            "disabled_at = {})"
            "".format(
                repr(self.id),
                repr(self.public_id),
                repr(self.company_name),
                repr(self.url),
                repr(self.role),
                repr(self.contacts),
                repr(self.description),
                repr(self.status),
                repr(self.reference),
                repr(self.current_stage_id),
                repr(self.created_at),
                repr(self.updated_at),
                repr(self.disabled_at),
            )
        )
