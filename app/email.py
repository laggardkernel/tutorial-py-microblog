#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread
from flask import current_app
from flask_mail import Message
from app import mail


def send_async_email(app, msg):
    # activate context and send an email
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body, attachments=None, sync=False):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    if attachments:
        for attachment in attachments:
            # :attachment: tuple (name, mime, data)
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        # get the real app object from proxy current_app
        Thread(target=send_async_email,
               args=(current_app._get_current_object(), msg)).start()
