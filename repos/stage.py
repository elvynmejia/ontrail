from .base import BaseRepo
from models import Stage
from entities import StageEntity


class StageRepo(BaseRepo):
    """ LeadRepo """

    @classmethod
    def model(cls):
        return Stage

    @classmethod
    def entity(cls):
        raise StageEntity
