from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo, StageRepo


start_at = datetime.utcnow()
end_at = datetime.utcnow()


def get_params(lead_id=None):
    return {
        "title": "Gloria <> Elvyn | Technical",
        "links": "",
        "description": "See how you go about solving a technical problem",
        "notes": "",
        "lead_id": lead_id,
        "state": "phone_screen",
        "start_at": start_at,
        "end_at": end_at,
    }


class TestUpdate(TestBase):        
    def test_success(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        params = get_params(lead.id)

        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.id),
            json={
                **{
                    **params,
                    "start_at": start_at.isoformat(),
                    "end_at": end_at.isoformat(),
                    "state": "onsite",
                },
            },
        )
        assert response.status_code == 200


    def test_not_found(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        params = get_params(lead.id)

        response = self.client.patch(
            "v1/stages/{}".format(100),
            json={
                **{
                    **params,
                    "start_at": start_at.isoformat(),
                    "end_at": end_at.isoformat(),
                    "state": "onsite",
                },
            },
        )

        assert response.status_code == 404


    def test_missing_params(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        params = get_params(lead.id)

        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.id),
            json={"title": "missing other params"},
        )

        assert response.status_code == 422

    def test_invalid_start_at_param(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        params = get_params(lead.id)
        stage = StageRepo.create(**params)

        response = self.client.patch(
            "v1/stages/{}".format(stage.id),
            json={
                **{
                    **params,
                    "start_at": start_at.isoformat(),
                    "end_at": end_at, # don't call isoformat() on this so that it fails
                    "state": "offer",
                },
            },
        )

        assert response.status_code == 422
        assert "Invalid start_at or end_at datetime format" in response.get_json()["message"]
