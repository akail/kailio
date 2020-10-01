# -*- coding: utf-8 -*-

import os
import pathlib

basedir = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

TEMPLATES_AUTO_RELOAD = os.getenv("TEMPLATES_AUTO_RELOAD")

# Secrets
SECRET_KEY = os.getenv("SECRET_KEY")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD") or "password"

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
UPLOADED_IMAGES_DEST = basedir / "static/uploads/images"
UPLOADED_IMAGES_URL = "/static/uploads/images/"
UPLOADED_ALL_DEST = basedir / "static/uploads/files"
UPLOADED_ALL_URL = "/static/uploads/files/"

# my settings
POSTS_PER_PAGE = 5

HYVOR_TALK_WEBSITE = 1513

# CKEDITOR
CKEDITOR_ENABLE_CODESNIPPET = True
CKEDITOR_CODE_THEME = "zenburn"
CKEDITOR_SERVER_LOCAL = False

# MAIL Settings
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = int(os.getenv("MAIL_PORT"))
MAIL_USE_SSL = True
MAIL_DEFAULT_SENDER = "andrew@kail.io"
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
