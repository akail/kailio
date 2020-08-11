# -*- coding: utf-8 -*-

import os
import pathlib

basedir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

TEMPLATES_AUTO_RELOAD = os.getenv("TEMPLATES_AUTO_RELOAD")

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")

# Sqlalchemy settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

# Flask Security Settings
SECURITY_REGISTERABLE = False
ECURITY_CHANGEABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")

# flask uploads
UPLOADED_IMAGES_DEST = basedir/'static/images'
UPLOADED_IMAGES_URL = '/static/images/'

# my settings
POSTS_PER_PAGE = 5

HYVOR_TALK_WEBSITE = 1513

# CKEDITOR
CKEDITOR_ENABLE_CODESNIPPET = True
CKEDITOR_CODE_THEME = 'zenburn'
CKEDITOR_SERVER_LOCAL = False
