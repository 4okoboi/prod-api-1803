from flask import Flask
from flask_restx import Api
from .links.views import links_namespace
from .config.config import config_dict
from .database.db import database


def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    api = Api(app)

    app.config.from_object(config)

    api.add_namespace(links_namespace, path="/links")
    return app
