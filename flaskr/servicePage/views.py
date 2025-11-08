from flask import Blueprint, render_template
from .model.requestInfo import RequestTemplate

servicePageBp = Blueprint("servicePage", __name__, url_prefix="/service",
                          template_folder="templates", static_folder="static") 


@servicePageBp.route("/support")
def servicePage():
    return render_template("templateServicePage.html")

@servicePageBp.route("/support/management/maintenanceRequest")
def maintenanceRequestPage():   
    info = RequestTemplate.MAINTENANCE.value
    return render_template("templateRequestPage.html", info=info)

@servicePageBp.route("/support/management/incidentRequest")
def incidentRequestPage():   
    info = RequestTemplate.INCIDENT.value
    return render_template("templateRequestPage.html", info=info)