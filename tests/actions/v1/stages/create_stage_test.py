from datetime import datetime
from tests.test_base import TestBase
from repos import LeadRepo
from constants import DATETIME_FORMAT


class TestCreate(TestBase):
    def test_create_success(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "lead_id": lead.public_id,
                "state": "phone_screen",
                "start_at": datetime.utcnow().strftime(DATETIME_FORMAT),
                "end_at": datetime.utcnow().strftime(DATETIME_FORMAT),
            },
        )

        assert response.status_code == 201
        assert response.get_json()["stage"]["lead_id"] == lead.public_id

    def test_create_success_no_dates_given(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "lead_id": lead.public_id,
                "state": "phone_screen",
            },
        )

        assert response.status_code == 201
        assert response.get_json()["stage"]["lead_id"] == lead.public_id

    def test_create_missing_lead_id(self):
        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "state": "phone_screen",
                "start_at": datetime.utcnow().strftime(DATETIME_FORMAT),
                "end_at": datetime.utcnow().strftime(DATETIME_FORMAT),
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
                "start_at": datetime.utcnow().strftime(DATETIME_FORMAT),
                "end_at": datetime.utcnow().strftime(DATETIME_FORMAT),
                "lead_id": lead_id__does_not_exist,
            },
        )

        assert response.status_code == 404
        assert response.get_json()[
            "message"
        ] == "Cannot find Lead by given lead_id {}".format(lead_id__does_not_exist)

    def test_create_invalid_end_at(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        response = self.client.post(
            "/v1/stages",
            json={
                "title": "Gloria <> Elvyn | Technical",
                "links": "",
                "description": "See how you go about solving a technical problem",
                "notes": "",
                "state": "phone_screen",
                "start_at": datetime.utcnow().strftime(DATETIME_FORMAT),
                "end_at": datetime.utcnow().isoformat(),
                "lead_id": lead.public_id,
            },
        )

        assert response.status_code == 422
        assert "Invalid end_at datetime format" in response.get_json()["message"]
