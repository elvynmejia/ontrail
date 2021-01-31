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
