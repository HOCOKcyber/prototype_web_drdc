from flask import Blueprint, render_template

mainPageBp = Blueprint("mainPage", __name__, url_prefix="/mainPage", 
                             template_folder="templates", static_folder="static")

@mainPageBp.route("/createTask")
def createTask():
    return render_template("createTaskPage.html")

@mainPageBp.route("/submittedTask")
def submittedTask():
    return render_template("submittedTask.html")

@mainPageBp.route("/currentTask")
def currentTask():
    return render_template("currentTask.html")

@mainPageBp.route('/completedTask')
def completedTask():
    return render_template('completedTask.html')