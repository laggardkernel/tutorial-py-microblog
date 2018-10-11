#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('api', __name__)

# load submodules at the end to avoid circular dependency
from app.api import users, errors, tokens
