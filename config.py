#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

basedir = os.path.dirname(os.path.abspath(__file__))


class Config(object):
    """
    Store different configs in separate classes
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable signal of db changes

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = os.environ.get('ADMIN') or ['you-email@example.com']

    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'zh_CN']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
