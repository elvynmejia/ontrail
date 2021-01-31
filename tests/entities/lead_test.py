from datetime import datetime
from tests.test_base import TestBase
from entities import LeadEntity
from repos import LeadRepo, StageRepo


class TestLeadEntity(TestBase):
    def test_as_json_internal_true(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = LeadEntity.as_json(lead, internal=True)
        assert response["lead"]["id"] == lead.id
        assert response["lead"]["public_id"] == lead.public_id

    def test_as_json_internal_false(self):
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

        LeadRepo.update(id=lead.id, current_stage_id=stage.id)

        response = LeadEntity.as_json(lead)
        assert response["lead"]["id"] == lead.public_id
        assert response["lead"].get("public_id") == None
        assert response["lead"]["current_stage_id"] == stage.public_id
