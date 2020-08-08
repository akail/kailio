# -*- coding: utf-8 -*-

from flask import current_app, render_template, request
from webargs import fields
from webargs.flaskparser import use_args

from kailio import db
from kailio.blog import blog
from kailio.model import Post, Tag


@blog.route("/")
@use_args({"page": fields.Integer(missing=0), 'tag': fields.Str(required=False)}, location='query')
def index(args):
    """"""
    page = args['page']

    query = Post.query.order_by(Post.published_at.desc())

    if 'tag' in args:
        query = query.filter(Post.tags.any(Tag.name == args['tag']))

    pagination = query.paginate(page, current_app.config['POSTS_PER_PAGE'], False)

    return render_template("blog/index.html", pagination=pagination)


@blog.route("/<post_name>")
def post(post_name):
    """"""
    post = Post.query.filter_by(slug=post_name).first_or_404()
    post.hits += 1
    db.session.commit()
    return render_template("blog/post.html", post=post)
