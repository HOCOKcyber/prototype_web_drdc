from flask import Blueprint, request, redirect, render_template

authorizationBp = Blueprint("authorization", __name__, url_prefix="/authorization", 
                             template_folder="templates", static_folder="static")

@authorizationBp.get("/login")
def login():
    return render_template("authorizationPage.html")

@authorizationBp.post("/login")
def login_verification():
    name = request.form["username"]
    password = request.form["password"]

    if validPassword(name, password):
        return redirect("/currentTask")

    return render_template("authorizationPage.html")


def validPassword(name, password):
    # TODO реализовать эту функцию и вынести из views
    return True
