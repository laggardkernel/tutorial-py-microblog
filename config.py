#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

basedir = os.path.dirname(os.path.abspath(__file__))
# load_dotenv(os.path.join(basedir, '.env')) # built in Flask now


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
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['you-email@example.com']
    if os.environ.get('ADMIN'):
        ADMINS = [os.environ.get('ADMIN')] + ADMINS

    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'zh_CN']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')

    # Full-text search
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # log to stdout for heroku
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
