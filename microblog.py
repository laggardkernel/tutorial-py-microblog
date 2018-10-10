#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app import create_app, db, cli
from app.models import User, Post, Message, Notification

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    """
    Add additional context into flask shell
    :return: context dict
    """
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification}
