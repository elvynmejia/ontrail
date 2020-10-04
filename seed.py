from flask import Blueprint
from db_config import db
from models import Lead, Stage

seed_bp = Blueprint('seed', __name__)

@seed_bp.cli.command('create')
def create():
		lead_1 = Lead(name="Derbix", contacts="Sam L", description="AI startup based in San Francisco")
		db.session.add(lead_1)
		db.session.commit()

		stage_1 = Stage(lead_id=lead_1.id, title="Intro call")
		db.session.add(stage_1)
		db.session.commit()


		lead_2 = Lead(name="Gem", contacts="Einas Had", description="Recruiting platform startup based in San Francisco")
		db.session.add(lead_2)
		db.session.commit()

		stage_2 = Stage(lead_id=lead_2.id, title="Intro call")
		db.session.add(stage_2)
		db.session.commit()
