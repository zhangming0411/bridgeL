#!/usr/bin/env python
# coding: utf-8

import click
from flask import Flask


def create_app(config_name=None):
    app = Flask(__name__)
    config_name.init_app(app)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    click.echo('You got me.')
    return app
