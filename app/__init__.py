#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)  # access config with app.config
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
