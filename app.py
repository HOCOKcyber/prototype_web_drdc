from flask import Flask,render_template, redirect, request

app = Flask(__name__)


# Главная страница
@app.route("/createTask")
def createTask():
    return render_template("mainPage/createTaskPage.html")

@app.route("/submittedTask")
def submittedTask():
    return render_template("mainPage/submittedTask.html")

@app.route("/currentTask")
def currentTask():
    return render_template("mainPage/currentTask.html")

@app.get("/")
def authorization():
    return render_template("authorizationPage.html")

@app.post("/")
def verification():
    name = request.form["username"]
    password = request.form["password"]

    app.logger.debug(f'username: {name}')
    app.logger.debug(f'password: {password}')
    
    if validPassword(name, password):
        return redirect("/createTask")

    return render_template("authorizationPage.html")


@app.route("/forgot-password")
def passwordRecovery():
    return "<h1>В разработке</h1>"


def validPassword(name, password):
    # TODO("Релизовать авторизацию и скорее всего как-то это вынести")
    return True

# Сервисное обслуживание
@app.route("/service")
def servicePage():
    return render_template("servicePage/templateServicePage.html")

# Сервисное обслуживание
@app.route("/service/maintenanceRequest")
def maintenanceRequestPage():
    return render_template("servicePage/maintenanceRequest.html")
