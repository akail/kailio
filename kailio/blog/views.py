# -*- coding: utf-8 -*-

from flask import render_template

from kailio.blog import blog
from kailio.model import Post


@blog.route("/")
def index():
    """"""
    latest_posts = Post.query.order_by(Post.published_at.desc()).limit(3).all()

    return render_template("blog/index.html", posts=latest_posts)


@blog.route("/<post_name>")
def post(post_name):
    """"""
    post = Post.query.filter_by(slug=post_name).first_or_404()
    return render_template("blog/post.html", post=post)
