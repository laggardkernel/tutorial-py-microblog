#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import sys
import json
from rq import get_current_job
from flask import render_template
from dotenv import dotenv_values
from app import create_app, db, mail
from app.email import send_mail
from app.models import Task, Post, User

# push app context for RQ worker
app = create_app()
app.app_context().push()
# update config from .env manually
app.config.update(dict(dotenv_values('.flaskenv')))
app.config.update(dict(dotenv_values('.env')))
# print(app.config)
mail.init_app(app)


def example(seconds):
    job = get_current_job()
    print('Starting task')
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()
        print(i)
        time.sleep(1)
    job.meta['progress'] = 100
    job.save_meta()
    print('Task completed')


def _set_task_progress(progress):
    job = get_current_job()
    if job:
        job.meta['progress'] = progress
        job.save_meta()
        task = Task.query.get(job.get_id())
        task.user.add_notification('task_progress',
                                   {'task_id': job.get_id(), 'progress': progress})
        if progress >= 100:
            task.complete = True
        db.session.commit()


def export_posts(user_id):
    try:
        user = User.query.get(user_id)
        _set_task_progress(0)
        data = []
        i = 0
        total_posts = user.posts.count()
        for post in user.posts.order_by(Post.timestamp.asc()):
            data.append({'body': post.body, 'timestamp': post.timestamp.isoformat() + 'Z'})
            time.sleep(5)
            i += 1
            _set_task_progress(100 * i // total_posts)
        # send mail with data to user
        with app.app_context():
            send_mail('[Microblog] You blog posts',
                      sender=app.config['ADMINS'][0], recipients=[user.email],
                      text_body=render_template('email/export_posts.txt', user=user),
                      html_body=render_template('email/export_posts.html', user=user),
                      attachments=[
                          ('post.json', 'application/json', json.dumps({'posts': data}, indent=4))
                      ],
                      sync=True)
    except:
        _set_task_progress(100)
        app.logger.error('Unhandled exception', exc_info=sys.exc_info())
