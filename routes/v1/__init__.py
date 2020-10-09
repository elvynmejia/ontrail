from flask import Blueprint

from actions.v1.leads import (
    Create as CreateLead,
    List as ListLeads,
    Show as ShowLead,
    Update as UpdateLead,
)

routes_bp = Blueprint("routes", __name__)

# leads API
routes_bp.add_url_rule(
    "/v1/leads", view_func=ListLeads.as_view("vi_leads_list"), methods=["GET"]
)

routes_bp.add_url_rule(
    "/v1/leads", view_func=CreateLead.as_view("vi_leads_post"), methods=["POST"]
)
routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=UpdateLead.as_view("vi_leads_patch"), methods=["PATCH"]
)
routes_bp.add_url_rule(
    "/v1/leads/<id>", view_func=ShowLead.as_view("vi_leads_show"), methods=["GET"]
)
