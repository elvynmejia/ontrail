from tests.test_base import TestBase
from repos import LeadRepo
from repos import StageRepo
from datetime import datetime


class TestList(TestBase):
    def test_list_success(self):
        for x in range(3):
            lead = LeadRepo.create(
                company_name="Test {}".format(x),
                contacts="Elvyn M",
                description="Not gonna make it startup #{}".format(x),
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

            LeadRepo.update(id=lead.id, current_stage_id=stage.id)

        response = self.client.get("/v1/leads")

        assert response.status_code == 200
        assert "lead_" in response.get_json()["leads"][0]["id"]
        assert response.get_json()["leads"][0]["current_stage_id"] == stage.public_id
        assert len(response.get_json()["leads"]) == 3

    def test_list_filter_by_status(self):
        LeadRepo.create(
            company_name="Test Company",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        for x in range(3):
            lead = LeadRepo.create(
                company_name="Test {}".format(x),
                contacts="Elvyn M",
                description="Not gonna make it startup #{}".format(x),
                role="Software Engineer",
                status="offer",
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

            LeadRepo.update(id=lead.id, current_stage_id=stage.id)

        response = self.client.get("/v1/leads", query_string={"status": "offer"})
        assert response.status_code == 200
        assert "lead_" in response.get_json()["leads"][0]["id"]
        assert response.get_json()["leads"][0]["current_stage_id"] == stage.public_id
        assert len(response.get_json()["leads"]) == 3

    def test_list_filter_by_status_invalid(self):
        LeadRepo.create(
            company_name="Test Company",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )
        response = self.client.get("/v1/leads", query_string={"status": "invalid"})
        assert response.status_code == 422

    def test_list_filter_by_url(self):
        lead = LeadRepo.create(
            company_name="Test Company",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )
        response = self.client.get("/v1/leads", query_string={"url": lead.url})
        assert response.status_code == 200
        assert len(response.get_json()["leads"]) == 1
        assert response.get_json()["leads"][0]["url"] == lead.url
