from .base import BaseRepo
from models import Lead
from entities import LeadEntity


class LeadRepo(BaseRepo):
    """ LeadRepo """

    @classmethod
    def model(cls):
        return Lead

    @classmethod
    def entity(cls):
        raise LeadEntity
