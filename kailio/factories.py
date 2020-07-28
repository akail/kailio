import datetime
import random

import factory
from faker import Faker

from kailio import db
from kailio.model import Page, Post, User, Role

fake = Faker()

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    email = factory.Faker('email')
    password = factory.Faker('password')
    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    active = True

    @factory.post_generation
    def roles(obj, create, extracted, **kwargs):
        if not create:
            return

        obj.roles = [Role.query.first()]


class PageFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Page
        sqlalchemy_session = db.session

    title = factory.Faker('sentence', nb_words=4)
    content = factory.LazyAttribute(lambda p: ' '.join(fake.paragraphs(nb=3)))
    summary = factory.LazyAttribute(lambda p: ' '.join(fake.paragraphs(nb=1)))

    published = True
    created_at = factory.LazyFunction(datetime.datetime.now)
    updated_at = factory.LazyFunction(datetime.datetime.now)
    published_at = factory.LazyFunction(datetime.datetime.now)

    @factory.post_generation
    def slug(obj, create, extracted, **kwargs):
        if not create:
            return
        obj.slug = extracted or obj.title.lower().replace(' ', '_').replace('.', '')

    @factory.post_generation
    def author(obj, create, extracted, **kwargs):
        if not create:
            return

        obj.author = random.choice(User.query.all())
        
        

class PostFactory(PageFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
