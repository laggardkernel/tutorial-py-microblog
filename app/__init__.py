#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: laggard
# @Date:   2018-08-08 16:17:11
# @Last Modified by:   laggardkernel
# @Last Modified time: 2018-08-08 16:27:26
from flask import Flask

app = Flask(__name__)

from app import routes
