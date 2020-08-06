# -*- coding: utf-8 -*-

from flask import render_template, request
from webargs import fields
from webargs.flaskparser import use_args

from kailio import db
from kailio.blog import blog
from kailio.model import Post


@blog.route("/")
@use_args({"page": fields.Integer(missing=0)}, location='query')
def index(args):
    """"""
    print(args)
    latest_posts = Post.query.order_by(Post.published_at.desc()).limit(5).all()

    return render_template("blog/index.html", posts=latest_posts)


@blog.route("/<post_name>")
def post(post_name):
    """"""
    post = Post.query.filter_by(slug=post_name).first_or_404()
    post.hits += 1
    db.session.commit()
    return render_template("blog/post.html", post=post)
