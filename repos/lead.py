from .base import BaseRepo
import models
import entities


class LeadRepo(BaseRepo):
    """ LeadRepo """

    @classmethod
    def model(cls):
        return models.Lead

    @classmethod
    def entity(cls):
        return entities.LeadEntity
