# -*- coding: utf-8 -*-

from flask import render_template

from kailio.main import main
from kailio.model import Page, Post


@main.route("/")
def index():
    """"""

    latest_post = Post.query.order_by(Post.published_at.desc()).first()
    popular_post = Post.query.order_by(Post.hits.desc()).first()
    return render_template(
        "index.html", latest_post=latest_post, popular_post=popular_post
    )


@main.route("/cv")
def cv():
    """"""
    return render_template("cv.html")


@main.route("/contact")
def contact():
    """"""
    # TODO: Should have a form AAK 2020-06-11

    return render_template("contact.html")


@main.route("/about")
def about():
    """"""
    return render_template("about.html")


@main.route("/portfolio")
def portfolio():
    """"""
    return render_template("portfolio.html")


@main.route("/<page_slug>")
def page(page_slug):
    page = Page.query.filter_by(slug=page_slug).first_or_404()
    return render_template("page.html", page=page)
