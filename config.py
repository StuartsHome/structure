import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    # Add SQLALCHEMY_DATABASE_URI field to the Config() class in your config.py file
    # to set your app to use the newly created database in development (local), staging, and production:
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']



class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True