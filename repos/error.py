class RepoErrorBase(BaseException):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)


class ArgumentError(RepoErrorBase):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)


class RecordNotFound(RepoErrorBase):
    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return "{}".format(self.message)
