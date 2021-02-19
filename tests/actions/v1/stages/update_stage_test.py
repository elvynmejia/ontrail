from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo, StageRepo
from constants import DATETIME_FORMAT


start_at = datetime.utcnow().strftime(DATETIME_FORMAT)
end_at = datetime.utcnow().strftime(DATETIME_FORMAT)


def get_params(lead_id=None):
    return {
        "title": "Gloria <> Elvyn | Technical",
        "links": "",
        "description": "See how you go about solving a technical problem",
        "notes": "",
        "lead_id": lead_id,
        "state": "scheduled",
        "start_at": start_at,
        "end_at": end_at,
    }


class TestUpdate(TestBase):
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        params = get_params(lead.id)

        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.public_id),
            json={
                **{
                    **params,
                    "start_at": start_at,
                    "end_at": end_at,
                    "state": "completed",
                    "lead_id": lead.public_id,
                },
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

        params = get_params(lead.id)

        response = self.client.patch(
            "v1/stages/{}".format("lead_100"),
            json={
                **{
                    **params,
                    "start_at": start_at,
                    "end_at": end_at,
                    "state": "onsite",
                    "lead_id": lead.public_id,
                },
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

        params = get_params(lead.id)

        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.public_id),
            json={"title": "missing other params", "lead_id": lead.public_id},
        )

        assert response.status_code == 422

    def test_success_no_dates_given(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        params = get_params(lead.id)
        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.public_id),
            json={
                **{**params, "state": "in_progress", "lead_id": lead.public_id},
            },
        )
        assert response.status_code == 200

    def test_success_invalid_end_at(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        params = get_params(lead.id)
        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.public_id),
            json={
                **{
                    **params,
                    "state": "in_progress",
                    "end_at": datetime.utcnow().isoformat(),
                    "lead_id": lead.public_id,
                },
            },
        )

        assert response.status_code == 422
        assert "Invalid end_at datetime format" in response.get_json()["message"]
