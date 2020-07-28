import datetime

from flask_security import RoleMixin, UserMixin

from kailio import db

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.name}"

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    username = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f"{self.email}"


tags_pages = db.Table('tags_pages',
                      db.Column('page_id', db.Integer(), db.ForeignKey('pages.id')),
                      db.Column('tag_id', db.Integer(), db.ForeignKey('tags.id')))


class Page(db.Model):
    __tablename__ = 'pages'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(120))
    slug = db.Column(db.String(120), unique=True)
    summary = db.Column(db.String())
    published = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime(), default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime(), onupdate=datetime.datetime.utcnow)
    published_at = db.Column(db.DateTime())
    content = db.Column(db.String())

    author = db.relationship('User', backref=db.backref('pages', lazy='dynamic'))
    tags = db.relationship('Tag', secondary=tags_pages,
                           backref=db.backref('pages', lazy='dynamic'))

    __mapper_args__ = {
        'polymorphic_on': type,
        'polymorphic_identity': 'page'
    }

    def __repr__(self):
        return f"{self.title}"


class Post(Page):
    __mapper_args__ = {
        'polymorphic_identity': 'post'
    }


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.name}"
