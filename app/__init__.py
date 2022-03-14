from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_migrate import Migrate
import os
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_login import LoginManager



# define new database
db = SQLAlchemy()  # database object
photos = UploadSet('photos',IMAGES)
UPLOAD_FOLDER = 'static/photos/'
login_manager = LoginManager()
migrate = Migrate()
# provides different security levels and by setting it to strong will monitor the changes in a user's request header and log the user out.
login_manager.session_protection = 'strong'


bootstrap = Bootstrap()








def create_app(config_name):

    # Initializing application
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'fhbhbghbg hreiuehfuhr'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:kimachas@localhost/pitch'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()

    # ....
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # registering Auth
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    # configure UploadSet
    configure_uploads(app,photos)
    #app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
    # photos = UploadSet('photos', IMAGES)


    # Initializing Flask Extensions
    bootstrap.init_app(app)

    app.config['SECRET_KEY'] ='no474tghff8735757t5hf75t77t8'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:kimachas@localhost/blog'
    db.init_app(app)
    login_manager.init_app(app)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    from .models import User, Blog
    

    

    return app
