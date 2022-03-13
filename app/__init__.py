from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# define new database
db = SQLAlchemy()  # database object
DB_NAME = "blog"  # database name


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
