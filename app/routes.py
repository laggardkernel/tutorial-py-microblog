# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-08-08 16:29:05
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-08-08 16:56:14
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'laggardkernel'}
    return render_template('index.html', title='Home', user=user)
