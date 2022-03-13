from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from .auth import db



# define new database
db = SQLAlchemy()  # database object
DB_NAME = "blog"  # database name

bootstrap = Bootstrap()
# Initializing application
app = Flask(__name__)







def create_app(config_name):
    # ....
    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth, url_prefix='/')

    # Initializing Flask Extensions
    bootstrap.init_app(app)

    app.config['SECRET_KEY'] ='no474tghff8735757t5hf75t77t8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:kimachas@localhost/blog'
    db.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    from .models import User, Blog
    create_database(app)

    

    return app
