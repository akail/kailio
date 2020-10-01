# -*- coding: utf-8 -*-
__version__ = "0.1.0"

import datetime
from pathlib import Path


from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask_admin import Admin
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads, patch_request_class, ALL


bootstrap = Bootstrap()
db = SQLAlchemy()
security = Security()
migrate = Migrate()
admin = Admin(name="kailio", template_mode="bootstrap3")
ckeditor = CKEditor()
mail = Mail()
moment = Moment()
images = UploadSet("images", IMAGES)
files = UploadSet("all", ALL)


def create_app(env_file=None):
    """Application Factory."""
    if env_file:
        load_dotenv(dotenv_path=Path(env_file))
    else:
        load_dotenv(find_dotenv())

    app = Flask(__name__)
    app.config.from_object("kailio.settings")

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    ckeditor.init_app(app)
    moment.init_app(app)
    configure_uploads(app, (images, files))
    patch_request_class(app, 16 * 1024 * 1024)
    mail.init_app(app)

    from kailio.model import User, Role

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    from kailio.main import main as main_blueprint

    app.register_blueprint(main_blueprint)

    from kailio.blog import blog as blog_blueprint

    app.register_blueprint(blog_blueprint)

    from kailio.crm import crm as crm_blueprint

    app.register_blueprint(crm_blueprint)

    from kailio.admin import register_admin_pages

    register_admin_pages(app)

    from kailio.cli import register_cli

    register_cli(app)

    @app.before_first_request
    def create_user():

        if not Role.query.filter_by(name="admin").first():
            admin_role = Role(name="admin", description="Admin user account")
            db.session.add(admin_role)
            db.session.commit()

        if not User.query.filter_by(email="andrew@kail.io").first():
            user_datastore.create_user(  # nosec
                email="andrew@kail.io",
                password=app.config["ADMIN_PASSWORD"],
                roles=[admin_role],
            )

        db.session.commit()

    from kailio import model

    @app.shell_context_processor
    def make_shell_context():
        return dict(
            db=db,
            User=model.User,
            Role=model.Role,
            Page=model.Page,
            Post=model.Post,
            Image=model.Image,
        )

    return app
