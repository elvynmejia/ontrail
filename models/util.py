from os import environ, path
from dotenv import load_dotenv
from uuid import uuid4

import models


def generate_public_id(context, cls, prefix):
    public_id = "{}_{}".format(prefix, uuid4().hex)

    # keep generating a public_id until we find a unique value
    while len(cls.query.filter_by(public_id=public_id).all()) > 0:
        public_id = "{}_{}".format(prefix, uuid4().hex)

    return public_id

def generate_url():
    url = environ["TRACKIT_URL"] + "/leads?url={}".format(uuid4().hex)
    # keep generating a public_id until we find a unique value
    while len(models.Lead.query.filter_by(url=url).all()) > 0:
        url = environ["TRACKIT_URL"] + "/leads?url={}".format(uuid4().hex)

    return url
