from uuid import uuid4


def generate_public_id(context, cls):
    # import pdb; pdb.set_trace()
    public_id = None
    while True:
        public_id = "lead_{}".format(uuid4().hex)

        if cls.query.filter_by(public_id=public_id).all() != None:
            break

    return public_id
