from datetime import datetime

from db_config import db
from constants import STAGE_STATUSES
from entities import StageEntity
from models.lead import Lead
from .util import generate_public_id


class Stage(db.Model):
    __tablename__ = "stages"
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    public_id = db.Column(
        db.String(32),
        nullable=False,
        default=lambda context: generate_public_id(context, Stage, "stage"),
        unique=True,
    )

    title = db.Column(
        db.String(100),
        nullable=False,
    )

    links = db.Column(db.Text(400), nullable=True)

    description = db.Column(db.Text(400), nullable=True)

    notes = db.Column(db.Text(400), nullable=True)

    lead_id = db.Column(db.Integer, db.ForeignKey(Lead.id), nullable=False)

    state = db.Column(
        db.String(100), nullable=False, default=STAGE_STATUSES["unscheduled"]
    )
    # relationships
    # this is problematic right now
    # lead = db.relationship(
    #     'Lead',
    #     backref="stage"
    # )

    reference = db.Column(db.String(100), nullable=True)

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )

    start_at = db.Column(db.DateTime, nullable=True)

    end_at = db.Column(db.DateTime, nullable=True)
    disabled_at = db.Column(db.DateTime, nullable=True)

    def as_json(self):
        return StageEntity().dump(self)

    def __repr__(self):
        return (
            "Stage(id = {}, public_id = {} title = {}, links = {} "
            "description = {}, notes = {}, lead_id = {} "
            "state = {}, reference = {}, created_at = {}, updated_at = {}, disabled_at = {})"
            "".format(
                repr(self.id),
                repr(self.public_id),
                repr(self.title),
                repr(self.links),
                repr(self.description),
                repr(self.notes),
                repr(self.lead_id),
                repr(self.state),
                repr(self.reference),
                repr(self.start_at),
                repr(self.end_at),
                repr(self.created_at),
                repr(self.updated_at),
                repr(self.disabled_at),
            )
        )
