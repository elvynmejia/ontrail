from datetime import datetime
from tests.test_base import TestBase
from repos import StageRepo, LeadRepo


class TestList(TestBase):
    def test_list_success(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        for x in range(3):
            StageRepo.create(
                **{
                    "title": "Gloria <> Elvyn | Technical",
                    "links": "",
                    "description": "See how you go about solving a technical problem",
                    "notes": "",
                    "lead_id": lead.id,
                    "state": "phone_screen",
                    "start_at": datetime.utcnow(),
                    "end_at": datetime.utcnow(),
                },
            )

        response = self.client.get("/v1/stages")

        assert response.status_code == 200
        assert response.get_json()["stages"][0]["id"] == 3
        assert len(response.get_json()["stages"]) == 3

    def test_list_by_lead_id_success(self):
        lead_1 = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        lead_2 = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        for x in range(5):
            StageRepo.create(
                **{
                    "title": "Stage {}".format(x),
                    "links": "",
                    "description": "See how you go about solving a technical problem",
                    "notes": "",
                    "lead_id": lead_1.id,
                    "state": "phone_screen",
                    "start_at": datetime.utcnow(),
                    "end_at": datetime.utcnow(),
                },
            )

        for x in range(3):
            StageRepo.create(
                **{
                    "title": "Gloria <> Elvyn | Technical",
                    "links": "",
                    "description": "See how you go about solving a technical problem",
                    "notes": "",
                    "lead_id": lead_2.id,
                    "state": "phone_screen",
                    "start_at": datetime.utcnow(),
                    "end_at": datetime.utcnow(),
                },
            )

        response = self.client.get("/v1/stages", query_string={"lead_id": lead_1.id})

        assert response.status_code == 200
        assert response.get_json()["stages"][0]["id"] == 5
        assert len(response.get_json()["stages"]) == 5
