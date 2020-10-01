# -*- coding: utf-8 -*-

import os
import uuid

from flask import abort, current_app, redirect, request, url_for, Markup
from flask_admin.contrib.sqla import ModelView
from flask_admin import form
from flask_ckeditor import CKEditorField
from flask_security import current_user
from werkzeug.utils import secure_filename

from kailio import admin, db, security
from kailio.model import User, Role, Page, Post, Tag, Image, File


class AdminModelView(ModelView):
    """Custom Admin model view with restrictions."""

    def is_accessible(self):
        return (
            current_user.is_active
            and current_user.is_authenticated
            and current_user.has_role("admin")
        )

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for("security.login", next=request.url))


class PageAdmin(AdminModelView):
    form_overrides = dict(content=CKEditorField)
    create_template = "admin/edit.html"
    edit_template = "admin/edit.html"
    column_exclude_list = ["type", "content", "summary"]
    form_excluded_columns = ["type"]


class RoleView(AdminModelView):
    can_delete = False


def _list_thumbnail(view, context, model, name):
    if not model.filename:
        return ""

    return Markup('<img src="{model.url}" style="width: 150px;">'.format(model=model))


def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename("{}{}".format(uid, ext))


def register_admin_pages(app):
    """
    :param app: Flask application
    """

    class ImageView(AdminModelView):

        column_list = ["image", "name", "filename", "size", "url"]

        column_formatters = {"image": _list_thumbnail}

        form_extra_fields = {
            "filename": form.ImageUploadField(
                "Image",
                base_path=app.config["UPLOADED_IMAGES_DEST"],
                url_relative_path="images/",
                namegen=_imagename_uuid1_gen,
            )
        }

    class FileView(AdminModelView):

        column_list = ["file", "name", "filename", "size", "url"]

        form_extra_fields = {
            "filename": form.FileUploadField(
                "File",
                base_path=app.config["UPLOADED_ALL_DEST"],
                namegen=_imagename_uuid1_gen,
            )
        }

    admin.add_view(AdminModelView(User, db.session))
    admin.add_view(RoleView(Role, db.session))
    admin.add_view(PageAdmin(Page, db.session))
    admin.add_view(PageAdmin(Post, db.session))
    admin.add_view(AdminModelView(Tag, db.session))
    admin.add_view(ImageView(Image, db.session))
    admin.add_view(FileView(File, db.session))
