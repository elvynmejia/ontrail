from db_config import db

STATUSES = {
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
    name = db.Column(db.String, nullable=False)

    contacts = db.Column(db.String, nullable=False)

    description = db.Column(db.Text, nullable=True)

    status = db.Column(db.String, nullable=False, default=STATUSES.get("unscheduled"))

    # relationships
    stages = db.relationship("Stage", backref="lead", lazy="dynamic")

    def __repr__(self):
        return (
            "Lead(id = {}, name = {}, contacts = {}, description = {}"
            "status = {})"
            "".format(
                repr(self.id),
                repr(self.name),
                repr(self.contacts),
                repr(self.description),
                repr(self.status),
            )
        )
