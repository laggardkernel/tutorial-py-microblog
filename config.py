#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


class Config(object):
    """
    Store different configs in separate classes
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
