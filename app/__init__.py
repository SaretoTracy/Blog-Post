from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_login import LoginManager



# define new database
db = SQLAlchemy()  # database object

login_manager = LoginManager()
# provides different security levels and by setting it to strong will monitor the changes in a user's request header and log the user out.
login_manager.session_protection = 'strong'


login_manager.login_view = 'auth.login'


bootstrap = Bootstrap()








def create_app(config_name):

    # Initializing application
    app = Flask(__name__)
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
    

    

    return app
