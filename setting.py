#!/usr/bin/env python
# coding: utf-8

import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'I am the secret of bridge.'
    FILE_DIR = u'/Users/zhangming/resources'  # 地址用unicode，那么os.listdir函数就会返回unicode；如果用utf8，中文就会报错

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
