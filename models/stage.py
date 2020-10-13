from db_config import db
from models.lead import STATES


class Stage(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True,
        nullable=False,
    )

    title = db.Column(
        db.String,
        nullable=False,
    )

    links = db.Column(db.Text, nullable=True)

    description = db.Column(db.Text, nullable=True)

    notes = db.Column(db.Text, nullable=True)

    lead_id = db.Column(db.Integer, db.ForeignKey("lead.id"), nullable=False)

    state = db.Column(db.String, nullable=False, default=STATES["phone_screen"])
    # relationships
    # this is problematic right now
    # lead = db.relationship(
    #     'Lead',
    #     backref="stage"
    # )

    def __repr__(self):
        return (
            "Stage(id = {}, title = {}, links = {}"
            "description = {}, notes = {}, lead_id = {})"
            "status = {}"
            "".format(
                repr(self.id),
                repr(self.title),
                repr(self.links),
                repr(self.description),
                repr(self.notes),
                repr(self.lead_id),
                repr(self.status),
            )
        )
