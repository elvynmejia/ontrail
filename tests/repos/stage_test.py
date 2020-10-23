from datetime import datetime
from tests.test_base import TestBase
from models.stage import STATES
from repos import StageRepo, LeadRepo


class TestStageRepo(TestBase):
    def test_create_default_status(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        stage = StageRepo.create(
            title="phone screen with Gloria",
            description="See if there's match",
            lead_id=lead.id,
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
        )

        assert stage.title == "phone screen with Gloria"
        assert stage.description == "See if there's match"
        assert stage.lead_id == lead.id
        assert stage.state == "phone_screen"

    def test_create_with_phone_screen_status(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        stage = StageRepo.create(
            title="phone screen with Gloria",
            description="See if there's match",
            lead_id=lead.id,
            state=STATES["phone_screen"],
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
        )

        assert stage.title == "phone screen with Gloria"
        assert stage.description == "See if there's match"
        assert stage.lead_id == lead.id
        assert stage.state == STATES["phone_screen"]

    def test_find(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        stage_1 = StageRepo.create(
            title="phone screen with Gloria",
            description="See if there's match",
            lead_id=lead.id,
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
        )

        stage = StageRepo.find(id=stage_1.id)

        assert stage.id == stage_1.id

    def test_find_all(self):
        stages = StageRepo.find_all()
        # TODO: reset the database to a pristine state after every test case
        assert len(stages) == 3

    def test_update(self):
        lead = LeadRepo.create(
            company_name="Test",
            contacts="Elvyn M",
            description="Not gonna make it startup",
        )

        stage_1 = StageRepo.create(
            title="phone screen with Gloria",
            description="See if there's match",
            lead_id=lead.id,
            start_at=datetime.utcnow(),
            end_at=datetime.utcnow(),
        )
        updated_stage = StageRepo.update(id=lead.id, title="changedme")
        assert updated_stage.title == "changedme"
