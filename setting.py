#!/usr/bin/env python
# coding: utf-8

import os


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I am the secret of bridge.'

    @staticmethod
    def init_app(app):
        pass
