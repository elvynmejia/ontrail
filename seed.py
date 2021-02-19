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
        role="Sr Backend Engineer",
    )

    stage = StageRepo.create(
        title="Gloria <> Elvyn | Technical",
        links="",
        description="See how you go about solving a technical problem",
        notes="",
        lead_id=lead.id,
        state="unscheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    StageRepo.create(
        title="Gloria <> Elvyn | Technical",
        links="",
        description="See how you go about solving a technical problem",
        notes="",
        lead_id=lead.id,
        state="completed",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    # assign a current stage
    LeadRepo.update(id=lead.id, current_stage_id=stage.id)

    lead_1 = LeadRepo.create(
        company_name="Gem",
        contacts="Elvyn M",
        description="Not gonna make it startup",
        role="Software Engineer",
    )

    for x in range(5):
        StageRepo.create(
            title="Gloria {} <> Elvyn | Technical".format(x),
            links="",
            description="See how you go about solving a technical problem {}".format(x),
            notes="",
            lead_id=lead_1.id,
            state="scheduled",
            start_at=datetime.utcnow().isoformat(),
            end_at=datetime.utcnow().isoformat(),
        )
