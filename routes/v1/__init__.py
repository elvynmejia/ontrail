from flask import Blueprint

from actions.v1.leads import (
    Create as CreateLead,
    List as ListLeads,
    Show as ShowLead,
    Update as UpdateLead,
    Delete as DeleteLead,
)

from actions.v1.stages import (
    Create as CreateStage,
    List as ListStages,
    Show as ShowStage,
    Update as UpdateStage,
)

routes_bp = Blueprint("routes", __name__)

# leads API
routes_bp.add_url_rule(
    "/v1/leads", view_func=ListLeads.as_view("v1_leads_list"), methods=["GET"]
)

routes_bp.add_url_rule(
    "/v1/leads", view_func=CreateLead.as_view("v1_leads_create"), methods=["POST"]
)

routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=UpdateLead.as_view("v1_leads_update"), methods=["PATCH"]
)

routes_bp.add_url_rule(
    "/v1/leads/<id>",
    view_func=DeleteLead.as_view("v1_leads_delete"),
    methods=["DELETE"],
)

routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=ShowLead.as_view("v1_leads_show"), methods=["GET"]
)


# stages API
routes_bp.add_url_rule(
    "/v1/stages", view_func=ListStages.as_view("v1_stages_list"), methods=["GET"]
)

routes_bp.add_url_rule(
    "/v1/stages", view_func=CreateStage.as_view("v1_stages_create"), methods=["POST"]
)

routes_bp.add_url_rule(
    "/v1/stages/<id>",
    view_func=UpdateStage.as_view("v1_stages_update"),
    methods=["PATCH"],
)

routes_bp.add_url_rule(
    "/v1/stages/<id>", view_func=ShowStage.as_view("v1_stages_show"), methods=["GET"]
)
