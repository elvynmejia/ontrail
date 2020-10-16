class ActionErrorBase(BaseException):
    def __init__(self, http_code=None, code=None, message="", errors=[]):
        self.http_code = http_code
        self.code = code
        self.message = message
        self.errors = errors
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)

    def as_json(self):
        return {
            "code": self.code,
            "htttp_code": self.http_code,
            "message": self.message,
            "errors": self.errors,
        }


class NotFound(ActionErrorBase):
    def __init__(
        self,
        http_code=404,
        code="NOT_FOUND",
        message="The requested resource could not be found",
        errors=[],
    ):
        super().__init__(http_code=http_code, code=code, message=message, errors=errors)


class UnprocessableEntity(ActionErrorBase):
    def __init__(
        self,
        http_code=422,
        code="UNPROCESSABLE_ENTITY",
        message="The request was well-formed but was unable to be followed due to semantic errors.",
        errors=[],
    ):
        super().__init__(http_code=http_code, code=code, message=message, errors=errors)


class Unauthorized(ActionErrorBase):
    def __init__(
        self,
        http_code=401,
        code="UNAUTHORIZED",
        message="Authentication is required",
        errors=[],
    ):
        super().__init__(http_code=http_code, code=code, message=message, errors=errors)
