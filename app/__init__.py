from flask import Flask


# Initializing application
app = Flask(__name__)



def create_app():
    # ....
    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth, url_prefix='/')

    return app
