# -*- coding: utf-8 -*-

from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField


from kailio import admin, db
from kailio.model import User, Role, Page, Post, Tag


class PageAdmin(ModelView):
    form_overrides = dict(content=CKEditorField)
    create_template = "admin/edit.html"
    edit_template = "admin/edit.html"
    column_exclude_list = ["type", "content", "summary"]
    form_excluded_columns = ["type"]


class RoleView(ModelView):
    can_delete = False


def register_admin_pages(app):
    """
    :param app: Flask application
    """
    admin.add_view(ModelView(User, db.session))
    admin.add_view(RoleView(Role, db.session))
    admin.add_view(PageAdmin(Page, db.session))
    admin.add_view(PageAdmin(Post, db.session))
    admin.add_view(ModelView(Tag, db.session))
