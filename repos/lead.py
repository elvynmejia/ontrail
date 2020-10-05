from .base import BaseRepo
from models import Lead


class LeadRepo(BaseRepo):
    """ LeadRepo """

    @classmethod
    def model(cls):
        return Lead
