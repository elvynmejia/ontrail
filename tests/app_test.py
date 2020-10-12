from test_base import TestBase
from db_config import db, migrate
import pytest
import pdb

class TestApp(TestBase):
    def test_create_app(self, mocker):
        mocker.patch("db_config.db.init_app")
        mocker.patch("db_config.migrate.init_app")
        assert self.app.config.get("SQLALCHEMY_DATABASE_URI") is not None
        assert self.app.config.get("TESTING") == True
        db.init_app.assert_called_once
        migrate.init_app.assert_called_once

    def test_health_check_ok(self):
        response = self.client.get("/health/ok")
        assert b"Ok" in response.data
        assert response.status_code == 200

    def test_health_check_boom(self):
        with pytest.raises(SystemError) as excinfo:
        		self.client.get("/health/boom")
        
