# -*- coding: utf-8 -*-

import os
import uuid

from flask import current_app, Markup
from flask_admin.contrib.sqla import ModelView
from flask_admin import form
from flask_ckeditor import CKEditorField
from werkzeug.utils import secure_filename

from kailio import admin, db
from kailio.model import User, Role, Page, Post, Tag, Image


class PageAdmin(ModelView):
    form_overrides = dict(content=CKEditorField)
    create_template = "admin/edit.html"
    edit_template = "admin/edit.html"
    column_exclude_list = ["type", "content", "summary"]
    form_excluded_columns = ["type"]


class RoleView(ModelView):
    can_delete = False


def _list_thumbnail(view, context, model, name):
    if not model.filename:
        return ''

    return Markup(
        '<img src="{model.url}" style="width: 150px;">'.format(model=model)
    )


def _imagename_uuid1_gen(obj, file_data):
    _, ext = os.path.splitext(file_data.filename)
    uid = uuid.uuid1()
    return secure_filename('{}{}'.format(uid, ext))


def register_admin_pages(app):
    """
    :param app: Flask application
    """

    class ImageView(ModelView):

        column_list = [
            'image', 'name', 'filename', 'size', 'url'
        ]

        column_formatters = {
            'image': _list_thumbnail
        }

        form_extra_fields = {
            'filename': form.ImageUploadField(
                'Image',
                base_path=app.config['UPLOADED_IMAGES_DEST'],
                url_relative_path='images/',
                namegen=_imagename_uuid1_gen,
            )
        }


    admin.add_view(ModelView(User, db.session))
    admin.add_view(RoleView(Role, db.session))
    admin.add_view(PageAdmin(Page, db.session))
    admin.add_view(PageAdmin(Post, db.session))
    admin.add_view(ModelView(Tag, db.session))
    admin.add_view(ImageView(Image, db.session))
