from datetime import datetime

from db_config import db

STATES = {
    "unscheduled": "unscheduled",  # kind of doesn't make sense
    "phone_screen": "phone_screen",
    "take_home_or_technical": "take_home_or_technical",
    "onsite": "onsite",
    "offer": "offer",
    "hired": "hired",
    "not_a_good_fit": "not_a_good_fit",  # for me or for them
}


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

    created_at = db.Column(db.String, nullable=False, default=datetime.utcnow())

    updated_at = db.Column(
        db.String, nullable=False, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )

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
