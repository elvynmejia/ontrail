from tests.test_base import TestBase
from repos import LeadRepo


class TestCreate(TestBase):
    def test_create_success(self):
        response = self.client.post(
            "/v1/leads",
            json={
                "company_name": "Gem",
                "position": "Senior Fullstack Engineer",
                "contacts": "Gloria",
            },
        )

        assert response.status_code == 201
        assert response.get_json()["lead"]["company_name"] == "Gem"

    def test_create_422(self):
        response = self.client.post(
            "/v1/leads",
            json={
                "position": "Senior Fullstack Engineer",
                "contacts": "Gloria",
            },
        )
        assert response.status_code == 422
        assert (
            response.get_json()["errors"][0]["company_name"][0]
            == "Field may not be null."
        )
