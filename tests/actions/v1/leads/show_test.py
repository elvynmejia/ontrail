from tests.test_base import TestBase
from repos import LeadRepo



class TestShow(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        response = self.client.get(
            "v1/leads/{}".format(lead.id),
        )

        assert response.status_code == 200
        assert response.get_json()["lead"]["id"] == lead.id

    def test_not_found(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        response = self.client.get(
            "v1/leads/{}".format(100),
        )

        assert response.status_code == 404

    def test_missing_id(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        response = self.client.get(
            "v1/leads/{}",
        )

        assert response.status_code == 422
        assert response.get_json()["message"] == "Missing required id"
