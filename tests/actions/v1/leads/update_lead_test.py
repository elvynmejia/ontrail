from tests.test_base import TestBase
from repos import LeadRepo


class TestUpdate(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.patch(
            "v1/leads/{}".format(lead.public_id),
            json={
                "company_name": "a new company",
                "contacts": lead.contacts,
                "status": lead.status,
                "role": "Software Engineer",
            },
        )

        assert response.status_code == 200

    def test_not_found(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.patch(
            "v1/leads/{}".format("lead_100"),
            json={
                "company_name": "a new company",
                "contacts": lead.contacts,
                "status": lead.status,
                "role": "Software Engineer",
            },
        )

        assert response.status_code == 404

    def test_missing_params(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.patch(
            "v1/leads/{}".format(lead.id),
            json={
                "company_name": "a new company",
            },
        )

        assert response.status_code == 422
