from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo, StageRepo


class TestShow(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Gem",
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

        response = self.client.get(
            "v1/stages/{}".format(stage.id),
        )

        assert response.status_code == 200
        assert response.get_json()["stage"]["id"] == stage.public_id
        assert response.get_json()["stage"]["lead_id"] == lead.public_id

    def test_not_found(self):
        response = self.client.get(
            "v1/stages/{}".format(100),
        )

        assert response.status_code == 404

    def test_missing_id(self):
        lead = LeadRepo.create(
            company_name="Gem",
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

        response = self.client.get(
            "v1/stages/{}",
        )

        assert response.status_code == 422
        assert response.get_json()["message"] == "Missing required id"
