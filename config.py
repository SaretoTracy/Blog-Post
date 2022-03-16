import os
class Config:
    '''
    General configuration parent class
    '''
    secret_key = 'no474tghff8735757t5hf75t77t8'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'evesambu57@gmail.com'
    MAIL_PASSWORD = 'titravic'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kimachas@localhost/blog'
    pass




class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

    
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
