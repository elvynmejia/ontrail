from tests.test_base import TestBase
from repos import LeadRepo


class TestList(TestBase):
    def test_list_success(self):
        for x in range(3):
            lead = LeadRepo.create(
                company_name="Test {}".format(x),
                contacts="Elvyn M",
                description="Not gonna make it startup #{}".format(x),
                position="Software Engineer",
            )
        response = self.client.get("/v1/leads")

        assert response.status_code == 200
        assert response.get_json()["leads"][0]["id"] == 3
        assert len(response.get_json()["leads"]) == 3
