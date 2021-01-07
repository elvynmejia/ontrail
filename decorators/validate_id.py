from functools import wraps

from validators import IdValidator
from actions.error import UnprocessableEntity


def validate_id(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        validation = IdValidator().validate(kwargs)

        if validation:
            error = UnprocessableEntity(message="Missing required id")
            return error.as_json(), error.http_code
        return f(*args, **kwargs)

    return decorated_function
