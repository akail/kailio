__version__ = '0.1.0'


from flask import Flask
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app():
    """Application Factory."""

    app = Flask(__name__)
    bootstrap.init_app(app)

    from kailio.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
