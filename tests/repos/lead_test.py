from tests.test_base import TestBase
from repos import LeadRepo


class TestLeadRepo(TestBase):
    def test_create(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        assert lead.company_name == "Test"
        assert lead.contacts == "Elvyn M"
        assert lead.description == "Not gonna make it startup"

    def test_find(self):
        lead_1 = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )

        lead = LeadRepo.find(id=lead_1.id)

        assert lead.id == lead_1.id

    def test_find_all(self):
        leads = LeadRepo.find_all()
        # TODO: reset the database to a pristine state after every test case
        assert len(leads) == 2

    def test_update(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
            role="Software Engineer",
        )
        updated_lead = LeadRepo.update(id=lead.id, company_name="changed")
        assert updated_lead.company_name == "changed"
        assert LeadRepo.find(id=lead.id).company_name == "changed"
