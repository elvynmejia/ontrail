from test_base import TestBase
import pdb


class TestApp(TestBase):
    def test_config(self): 
        assert self.app.config.get("SQLALCHEMY_DATABASE_URI") is not None
        assert self.app.config.get("TESTING") == True

    def test_health_check(self):
        response = self.client.get("/health/ok")
        assert b"Ok" in response.data
        assert response.status_code == 200
