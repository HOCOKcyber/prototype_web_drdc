from flask import Flask,redirect,url_for

def create_app():
    app = Flask(__name__,
                template_folder='core/templates',
                static_folder='core/static')

    from .authorization.views import authorizationBp
    from .mainPage.views import mainPageBp
    from .servicePage.views import servicePageBp
    app.register_blueprint(authorizationBp)
    app.register_blueprint(mainPageBp)
    app.register_blueprint(servicePageBp)

    @app.route("/")
    def toLoginPage():
        return redirect(url_for("authorization.login"))

    return app
