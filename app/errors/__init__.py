#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('errors', __name__, template_folder='templates')

# import at the bottom to avoid circular denpendencies
from app.errors import handlers
