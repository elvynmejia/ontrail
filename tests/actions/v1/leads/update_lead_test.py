from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo, StageRepo


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

    def test_current_stage_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        stage = StageRepo.create(
            title="Gloria <> Elvyn | Technical",
            links="",
            description="See how you go about solving a technical problem",
            notes="",
            lead_id=lead.id,
            state="phone_screen",
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
        )

        response = self.client.patch(
            "v1/leads/{}".format(lead.public_id),
            json={
                "company_name": "a new company",
                "contacts": lead.contacts,
                "status": lead.status,
                "role": "Software Engineer",
                "current_stage_id": stage.public_id,
            },
        )

        assert response.status_code == 200
        assert response.get_json()["lead"]["current_stage_id"] == stage.public_id

    def test_current_stage_failure(self):
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
                "current_stage_id": "stage_123",
            },
        )

        assert response.status_code == 404
        assert (
            response.get_json()["message"]
            == "Current Stage with current_stage_id stage_123 not found"
        )
