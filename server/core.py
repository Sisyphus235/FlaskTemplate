# -*- coding: utf8 -*-

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # load public default configuration
    app.config.from_object('config')
    # load private default configuration
    app.config.from_pyfile('default.py')

    setup_blueprints(app)

    @app.route('/')
    def index():
        return "<h1>This is an index page.<h1/>"

    return app


def setup_blueprints(app):
    from server.AI.view import blueprint as AI

    blueprints = [
        {'handler': AI, 'url_prefix': '/AI'}
    ]

    for bp in blueprints:
        app.register_blueprint(bp['handler'], url_prefix=bp['url_prefix'])
