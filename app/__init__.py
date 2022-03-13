from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy


# define new database
db = SQLAlchemy()  # database object
DB_NAME = "blog"  # database name


# Initializing application
app = Flask(__name__)

app.config['SECRET_KEY'] ='no474tghff8735757t5hf75t77t8'





def create_app():
    # ....
    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth, url_prefix='/')

    # Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    return app
