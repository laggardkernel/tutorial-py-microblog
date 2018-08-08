# -*- coding: utf-8 -*-
# @Author: laggardkernel
# @Date:   2018-08-08 16:29:05
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-08-08 16:29:49
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
