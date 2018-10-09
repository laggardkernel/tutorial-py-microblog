#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('auth', __name__, template_folder='templates')

from app.auth import routes
