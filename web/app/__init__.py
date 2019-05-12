from flask import Flask
from .extensions import (db, api)
from .routes import RepositorioResource


def create_app(config=None):
    app = Flask(__name__)

    app.config.from_object('config.settings')

    if config:
        app.config.update(config)

    load_extensions(app)

    return app


def load_extensions(app):
    db.init_app(app)
    api.init_app(app)
