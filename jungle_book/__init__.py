from os.path import join, dirname
from os import environ
from dotenv import load_dotenv
from flask import Flask
from .models import db
from .views import route_blueprint, oauth
from config import ProductionConfig, DevelopmentConfig

dotenv_path = join(dirname(__file__), '.env')  # Path to .env file
load_dotenv(dotenv_path)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""

    app = Flask(__name__)
    if app.config['ENV'] == "production":
        app.config.from_object(ProductionConfig())
    elif app.config['ENV'] == "development":
        app.config.from_object(DevelopmentConfig())
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    setup_app(app)

    return app


def setup_app(app):
    """Create tables if they do not exist already"""
    @app.before_first_request
    def create_all_tables():
        db.create_all()
    db.init_app(app)
    oauth.init_app(app)
    app.register_blueprint(route_blueprint, url_prefix="")
