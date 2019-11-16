import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Create config object class"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "key"
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    GOOGLE_CLIENT_ID = "810979674149-i58pjaopuunstb60n6j645nhb9mvk66e.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "DVVkppPgpEFDX5S7naVvLGjA"


class ProductionConfig(Config):
    """Config for production"""
    DEBUG = False


class StagingConfig(Config):
    '''Config for staging'''
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    '''Config for development'''
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    '''Config for testing'''
    TESTING = False
