from .base import BaseRepo
import models
import entities


class StageRepo(BaseRepo):
    """ LeadRepo """

    @classmethod
    def model(cls):
        return models.Stage

    @classmethod
    def entity(cls):
        return entities.StageEntity
