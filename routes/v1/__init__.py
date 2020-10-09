from flask import Blueprint

from actions.v1.leads import (
    Create as CreateLead,
    List as ListLeads,
    Show as ShowLead,
    Update as UpdateLead,
)

from actions.v1.stages import (
	Create as CreateStage
)

routes_bp = Blueprint("routes", __name__)

# leads API
routes_bp.add_url_rule(
    "/v1/leads", view_func=ListLeads.as_view("v1_leads_list"), methods=["GET"]
)

routes_bp.add_url_rule(
    "/v1/leads", view_func=CreateLead.as_view("v1_leads_post"), methods=["POST"]
)

routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=UpdateLead.as_view("v1_leads_patch"), methods=["PATCH"]
)

routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=ShowLead.as_view("v1_leads_show"), methods=["GET"]
)


# stages API
routes_bp.add_url_rule(
	  "/v1/stages", view_func=CreateStage.as_view("v1_stages_create"), methods=["POST"]
)