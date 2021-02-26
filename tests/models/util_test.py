from tests.test_base import TestBase
from models.util import generate_public_id, generate_url
from models.lead import Lead
from repos import LeadRepo



class TestUtil(TestBase):
    def test_generate_public_id(self):
        assert "lead_" in generate_public_id(Lead, Lead, "lead")

    def test_generate_url(self):
        assert "http://" in generate_url()
