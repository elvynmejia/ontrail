from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo


class TestCreate(TestBase):
    def test_create_success(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "lead_id": lead.id,
                "state": "phone_screen",
                "start_at": datetime.utcnow().isoformat(),
                "end_at": datetime.utcnow().isoformat(),
            },
        )

        assert response.status_code == 201
        assert response.get_json()["stage"]["lead_id"] == lead.id

    def test_create_missing_lead_id(self):
        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "state": "phone_screen",
                "start_at": datetime.utcnow().isoformat(),
                "end_at": datetime.utcnow().isoformat(),
            },
        )

        assert response.status_code == 422
        assert (
            response.get_json()["errors"][0]["lead_id"][0] == "Field may not be null."
        )

    def test_create_lead_id_not_found(self):
        lead_id__does_not_exist = 100
        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "state": "phone_screen",
                "start_at": datetime.utcnow().isoformat(),
                "end_at": datetime.utcnow().isoformat(),
                "lead_id": lead_id__does_not_exist,
            },
        )

        assert response.status_code == 404
        assert response.get_json()[
            "message"
        ] == "Cannot find Lead by given lead_id {}".format(lead_id__does_not_exist)
