from flask import FlasK

def create_app():
    app = FlasK(__name__)


    from routes.home_route import home_route
    app.register_blueprint(home_route)

    return app


