from uuid import uuid4


def generate_public_id(context, cls):
    public_id = "lead_{}".format(uuid4().hex)

    # keep generating a public_id until we find a unique value
    while len(cls.query.filter_by(public_id=public_id).all()) > 0:
        public_id = "lead_{}".format(uuid4().hex)

    return public_id
