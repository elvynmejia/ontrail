from tests.test_base import TestBase
from repos import LeadRepo
from datetime import datetime


class TestDeleteLead(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.delete(
            "v1/leads/{}".format(lead.public_id),
        )

        assert response.status_code == 204
        assert isinstance(LeadRepo.find(id=lead.id).disabled_at, datetime)

    def test_not_found(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.delete(
            "v1/leads/{}".format("lead_100"),
        )

        assert response.status_code == 404
