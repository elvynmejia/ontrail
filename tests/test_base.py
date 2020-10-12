import pytest
from os import path
from app import create_app, db


class TestBase:
    def setup_class(self):
        self.app = create_app(config="config.Test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def teardown_class(self):
        db.session.remove()
        db.drop_all()
