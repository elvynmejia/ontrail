from datetime import datetime
from tests.test_base import TestBase
from entities import StageEntity
from repos import LeadRepo, StageRepo


class TestStageEntity(TestBase):
    def test_as_json_internal_true(self):
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

        response = StageEntity.as_json(stage, internal=True)
        assert response["stage"]["id"] == stage.id
        assert response["stage"]["public_id"] == stage.public_id
        assert response["stage"]["lead_id"] == lead.id

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

        response = StageEntity.as_json(stage)
        assert response["stage"]["id"] == stage.public_id
        assert response["stage"].get("public_id") == None
        assert response["stage"]["lead_id"] == lead.public_id
