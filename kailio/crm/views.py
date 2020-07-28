# -*- coding: utf-8 -*-

from flask import render_template
from kailio.crm import crm

# TODO: Limit to crm users only AAK 2020-06-10
# TODO: Use a different base that doesn't have the banner and extra stuff AAK 2020-06-10


@crm.route("/")
def index():
    """"""
    return "crm"


@crm.route("/<post_name>")
def post(post_name):
    """"""
    return post_name
