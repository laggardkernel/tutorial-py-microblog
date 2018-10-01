#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    """
    Add additional context into flask shell
    :return: context dict
    """
    return {'db': db, 'User': User, 'Post': Post}
