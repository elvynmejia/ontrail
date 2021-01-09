from datetime import datetime
from tests.test_base import TestBase
from repos import StageRepo, LeadRepo
from constants import DATETIME_FORMAT


class TestList(TestBase):
    def test_list_success(self):
        lead = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            position="Software Engineer",
        )

        for x in range(3):
            stage = StageRepo.create(
                **{
                    "title": "Gloria <> Elvyn | Technical",
                    "links": "",
                    "description": "See how you go about solving a technical problem",
                    "notes": "",
                    "lead_id": lead.id,
                    "state": "phone_screen",
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
            position="Software Engineer",
        )

        lead_2 = LeadRepo.create(
            company_name="Gem",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            position="Software Engineer",
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
                    "reference": "lead_1",
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
                    "reference": "lead_2",
                },
            )

        response = self.client.get("/v1/stages", query_string={"lead_id": lead_1.id})

        assert response.status_code == 200
        stages = response.get_json()["stages"]
        for stage in stages:
            assert stage["lead_id"] == lead_1.id

        assert len(stages) == 5
