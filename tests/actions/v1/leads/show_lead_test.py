from tests.test_base import TestBase
from repos import LeadRepo


class TestShow(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.get(
            "v1/leads/{}".format(lead.public_id),
        )

        assert response.status_code == 200
        assert response.get_json()["lead"]["id"] == lead.public_id

    def test_not_found(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.get(
            "v1/leads/{}".format("lead_100"),
        )

        assert response.status_code == 404

    def test_missing_id(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.get(
            "v1/leads/{}",
        )

        assert response.status_code == 422
        assert response.get_json()["message"] == "Missing or invalid required id"
