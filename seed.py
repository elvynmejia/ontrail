from datetime import datetime
from flask import Blueprint
from db_config import db
from repos import LeadRepo, StageRepo

seed_bp = Blueprint("seed", __name__)


@seed_bp.cli.command("create")
def create():
    lead = LeadRepo.create(
        company_name="Gem",
        contacts="Elvyn M",
        description="Not gonna make it startup",
        position="Sr Backend Engineer"
    )

    StageRepo.create(
        title="Gloria <> Elvyn | Technical",
        links="",
        description="See how you go about solving a technical problem",
        notes="",
        lead_id=lead.id,
        state="phone_screen",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    lead_1 = LeadRepo.create(
        company_name="Gem",
        contacts="Elvyn M",
        description="Not gonna make it startup",
        position="Software Engineer"
    )

    for x in range(5):
        StageRepo.create(
            title="Gloria {} <> Elvyn | Technical".format(x),
            links="",
            description="See how you go about solving a technical problem {}".format(x),
            notes="",
            lead_id=lead_1.id,
            state="phone_screen",
            start_at=datetime.utcnow().isoformat(),
            end_at=datetime.utcnow().isoformat(),
        )
