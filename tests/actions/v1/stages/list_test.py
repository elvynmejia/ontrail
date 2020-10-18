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
            response = self.client.post(
                "/v1/stages",
                json={
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
