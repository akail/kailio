
from kailio import db
from kailio.factories import UserFactory, PageFactory, PostFactory

def register_cli(app):

    @app.cli.command('fakeit')
    def gen_fake_data():
        """Generate fake data for testing purposes."""

        for i in range(1):
            UserFactory()

        PageFactory()

        for i in range(10):
            PostFactory()

        db.session.commit()
