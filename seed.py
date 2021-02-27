from datetime import datetime
from flask import Blueprint
from db_config import db
from repos import LeadRepo, StageRepo
from constants import LEAD_STATUSES

seed_bp = Blueprint("seed", __name__)


@seed_bp.cli.command("create")
def create():
    lead = LeadRepo.create(
        company_name="Gem",
        contacts="Dottie G",
        description="The Platform for Modern Recruiting",
        role="Sr Backend Engineer",
        status=LEAD_STATUSES["unscheduled"],
    )

    stage = StageRepo.create(
        title="Technical screening with recruiter",
        links="",
        description="I would like to learn more about background, career goals and see if you are a good fit",
        notes="",
        lead_id=lead.id,
        state="scheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    StageRepo.create(
        title="Technical 1-hour coding session with an engineer",
        links="",
        description="""
            This is a pair-programming session with one of our engineers.
            He will present you with a real world problem and see how you go about solving it.""",
        notes="",
        lead_id=lead.id,
        state="unscheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    # assign a current stage
    LeadRepo.update(id=lead.id, current_stage_id=stage.id)

    lead_1 = LeadRepo.create(
        company_name="Mutiny",
        contacts="Gee Gee D",
        description="PERSONALIZE YOUR WEBSITE FOR EACH VISITOR",
        role="Software Engineer",
    )

    StageRepo.create(
        title="Phone call with recruiter",
        links="",
        description="Find out if there's a mutual interest in moving forward in the interviewing process",
        notes="",
        lead_id=lead_1.id,
        state="scheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    lead_2 = LeadRepo.create(
        company_name="OpenAI",
        contacts="Justin Loi",
        description="Discovering and enacting the path to safe artificial general intelligence",
        role="Backend Software Engineer",
        status=LEAD_STATUSES["phone_screen"],
    )

    StageRepo.create(
        title="Phone call",
        links="",
        description="Do you have time for a quick call this week?",
        notes="",
        lead_id=lead_2.id,
        state="scheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )

    lead_3 = LeadRepo.create(
        company_name="Moveworks",
        contacts="Zia Castillo",
        description="Advanced AI Built for the Enterprise",
        role="Senior Fullstack Engineer",
        status=LEAD_STATUSES["onsite"],
    )

    StageRepo.create(
        title="Virtual Onsite",
        links="",
        description="Panel style interview: 1hr coding, 1hr product/design, 1 hour with leadership",
        notes="",
        lead_id=lead_3.id,
        state="scheduled",
        start_at=datetime.utcnow().isoformat(),
        end_at=datetime.utcnow().isoformat(),
    )
