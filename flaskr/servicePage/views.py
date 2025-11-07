from flask import Blueprint, render_template

servicePageBp = Blueprint("servicePage", __name__, url_prefix="/service",
                          template_folder="templates", static_folder="static") 


@servicePageBp.route("/support")
def servicePage():
    return render_template("templateServicePage.html")

@servicePageBp.route("/support/maintenanceRequest")
def maintenanceRequestPage():
    return render_template("maintenanceRequest.html")