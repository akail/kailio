# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv, find_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(find_dotenv())

TEMPLATES_AUTO_RELOAD = os.getenv("TEMPLATES_AUTO_RELOAD")

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")

# Sqlalchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Flask Security Settings
SECURITY_REGISTERABLE = False
SECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
