from flask import Blueprint
main = Blueprint('main', __name__)

from kailio.main import views, errors
