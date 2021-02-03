from functools import wraps
from actions.error import UnprocessableEntity


def validate_public_id(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if len(kwargs.get("id", "").split("_")) == 1:
            error = UnprocessableEntity(message="Missing or invalid required id")
            return error.as_json(), error.http_code
        return f(*args, **kwargs)

    return decorated_function
