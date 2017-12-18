#!/usr/bin/env python
# coding: utf-8

import click
from app import create_app
from setting import Config


app = create_app(Config)

#
# @app.route('/')
# def hello_world():
#     return 'Hello world!'

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
